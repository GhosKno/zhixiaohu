from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from api.models import Question, Activity
from api.serializers import QuestionCreateSerializer, QuestionDetailSerializer, AnswerSerializer
from utils import mixins
from utils.views import GenericViewSet, error, success


# used for create or show user associated question
class QuestionViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'detail')

    def get_queryset(self):
        return Question.objects.all()

    def get_serializer_class(self):
        # just used for create
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        if self.action == 'get_answers':
            return AnswerSerializer
        return QuestionCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        question = self.get_object()
        if question is None:
            return error('no question found')
        if request.user.is_authenticated:
            count = request.user.profile \
                .watchedQuestion\
                .filter(title=question).count()
            question.is_watch = count
            question.answer_count = question.answers.count()
            question.watch_count = question.watchedUser.count()
        else:
            question.is_watch = False
        seri = self.get_serializer(question)
        question.visit_count+=1
        return success(seri.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route(methods=['GET'])
    def get_answers(self, request, pk):
        question = self.get_object()
        if question is None:
            return error("no topic found")
        if request.user.is_authenticated:
            profile = request.user.profile
            profile.history.add(question)
            profile.save()
        queryset = self.filter_queryset(question.answers.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for answer in page:
                profile = answer.author.profile
                answer.userSummary = profile
                answer.comment_count = answer.comments.count()
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def watch(self, request, pk=None):
        if request.user.is_authenticated is False:
            return error('please login')
        question = self.get_object()
        if question is None:
            return error('question not exists')
<<<<<<< HEAD
        if request.user.is_authenticated:
            Activity.watchQuestion(request.user.profile, question)
            profile = request.user.profile
            profile.watchedQuestion.add(question)
            profile.save()
            return success()
        return error('please login at first')
=======
        profile = request.user.profile
        profile.watchedQuestion.add(question)
        profile.save()
        Activity.watchQuestion(request.user.profile, question)
        return success()
>>>>>>> frontend: fetch answers in question page

    @detail_route(methods=['GET'])
    def cancel_watch(self, request, pk=None):
        if request.user.is_authenticated is False:
            return error('please login')
        question = self.get_object()
        if question is None:
            return error('question not exists')
        profile = request.user.profile
        profile.watchedQuestion.remove(question)
        profile.save()
        return success()
