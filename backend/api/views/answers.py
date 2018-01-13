from threading import Thread

from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from api.apps import ApiCli
from api.models import Answer, Message, Activity
from api.serializers import AnswerSerializer, CommentSerializer, AnswerCreateSerializer, AnswerUpdateSerializer
from api.utils.heat import HeatQueue
from api.utils import mixins
from api.utils.views import error, success, GenericViewSet


class AnswerViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
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
        if self.action == 'update':
            return AnswerUpdateSerializer
        return AnswerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for instance in page:
                ApiCli.process_answer(instance, request.user)
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']
            if question.answers.filter(author=request.user).exists():
                return error('你已经回答过该问题了')
            answer = self.perform_create(serializer)
            answer.userSummary = request.user.profile
            answer.has_favorite = False
            answer.has_approve = False
            answer.has_against = False
            answer.comment_count = answer.comments.count()
            seri = AnswerSerializer(answer, context={'request': request})
            return success(seri.data)
        key = list(serializer.errors.keys())[0]
        return error(key+': '+serializer.errors[key][0])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            ApiCli.process_answer(instance, request.user)
            serializer = self.get_serializer(instance)
            return success(serializer.data)
        return error('没有找到该回答')

    @detail_route(methods=['GET'])
    def get_comments(self, request, pk=None):
        answer = self.get_object()
        if answer is None:
            return error("没有找到该评论所在的回答")

        queryset = self.filter_queryset(answer.comments.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for comment in page:
                ApiCli.process_comment(comment)
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('没有更多了')

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
            return error('没有找到你想赞的回答')
        if profile.agreed.filter(id=answer.id).exists():
            return error('你已经赞过了')

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
            return error('没有找到你想取消赞的回答')
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
            return error('没有找到你想踩的回答')
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
            return error('没有找到你想取消踩的回答')
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
            return error('没有找到你想收藏的回答')
        profile.favorites.add(answer)
        profile.save()
        return success()

    @detail_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def cancel_favorite(self, request, pk=None):
        profile = request.user.profile
        answer = self.get_object()
        if answer is None:
            return error('没有找到你想取消收藏的回答')
        profile.favorites.remove(answer)
        profile.save()
        return success()


def add_message(rec, question, answer, author):
    message = Message.objects.create(receiver=rec,
                                     question=question,
                                     answer=answer,
                                     author=author)
    message.save()


def msg_thread(question, user, answer):
    q_users = question.watchedUser.all()
    u_users = user.watchedBy.all()

    users = q_users | u_users  # merge
    for rec in users:
        receiver = rec.user
        add_message(receiver, question, answer, user.profile)

    for topic in question.topics.all():
        HeatQueue.put(topic)
