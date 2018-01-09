from threading import Thread

from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from api.models import Answer, Message, Activity, Question
from api.serializers import AnswerSerializer, CommentSerializer, AnswerCreateSerializer
from utils.heat import HeatQueue
from utils.views import error, success, GenericViewSet
from utils import mixins


class AnswerViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    filter_backends = (SearchFilter,)
    search_fields = ('detail',)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AnswerCreateSerializer
        if self.action == 'get_comments':
            return CommentSerializer
        return AnswerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                instance.userSummary = instance.author.profile
                instance.comment_count = instance.comments.count()
                user = request.user
                if user.is_authenticated:
                    instance.has_approve = user.profile.agreed.filter(id=instance.id).exists()
                    instance.has_against = user.profile.disagreed.filter(id=instance.id).exists()
                else:
                    instance.has_approve = False
                    instance.has_against = False
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_id = serializer.validated_data['question']
        question = Question.objects.get(id=question_id)
        if question.answers.filter(author=request.user).exists():
            return error('you already answered this question')
        answer = self.perform_create(serializer)
        answer.userSummary = request.user.profile
        answer.has_favorite = False
        seri = AnswerSerializer(answer, context={'request': request})
        headers = self.get_success_headers(seri.data)
        return Response({'success': True, 'data': seri.data}, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.userSummary = instance.author.profile
            instance.comment_count = instance.comments.count()
            user = request.user
            if user.is_authenticated:
                instance.has_approve = user.profile.agreed.filter(id=instance.id).exists()
                instance.has_against = user.profile.disagreed.filter(id=instance.id).exists()
                instance.has_favorite = user.profile.favorites.filter(id=instance.id).exists()
            else:
                instance.has_approve = False
                instance.has_against = False
                instance.has_favorite = False
            serializer = self.get_serializer(instance)
            return success(serializer.data)
        return error('cant found')

    @detail_route(methods=['GET'])
    def get_comments(self, request, pk=None):
        answer = self.get_object()
        if answer is None:
            return error("no answer found")

        queryset = self.filter_queryset(answer.comments.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for comment in page:
                profile = comment.author.profile
                comment.userSummary = profile
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    def perform_create(self, serializer):
        user = self.request.user
        user.profile.answerCount += 1
        user.profile.save()
        question = serializer.validated_data['question']
        answer = serializer.save(author=user)
        thread = Thread(target=msg_thread, args=(question, user, answer))
        thread.start()
        return answer

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
    def agree(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        answer.approve += 1
        answer.save()
        profile.agreed.add(answer)
        profile.save()
        if request.user.is_authenticated:
            Activity.agreeAnswer(request.user.profile, answer)
        return success()

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
    def cancel_agree(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        answer.approve -= 1
        answer.save()
        profile.agreed.remove(answer)
        profile.save()
        return success()

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
    def disagree(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        answer.against += 1
        answer.save()
        profile.disagreed.add(answer)
        profile.save()
        return success()

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
    def cancel_disagree(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        answer.against -= 1
        answer.save()
        profile.disagreed.remove(answer)
        profile.save()
        return success()

    @detail_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        profile.favorites.add(answer)
        profile.save()
        return success()

    @detail_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def cancel_favorite(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('no answer found')
        profile.favorites.remove(answer)
        profile.save()
        return success()


def addMessageForUser(rec, question, answer, author):
    message = Message.objects.create(receiver=rec,
                                     question=question,
                                     answer=answer,
                                     author=author)
    message.save()
    return True


def msg_thread(question, user, answer):
    q_users = question.watchedUser.all()
    u_users = user.watchedBy.all()

    users = q_users | u_users  # merge
    for rec in users:
        receiver = rec.user
        addMessageForUser(receiver, question, answer, user)
    for topic in question.topics.all():
        HeatQueue.put(topic)
