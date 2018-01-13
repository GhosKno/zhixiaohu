from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from api.apps import ApiCli
from api.models import Question, Activity
from api.serializers import QuestionCreateSerializer, QuestionDetailSerializer, AnswerSerializer
from api.utils import mixins
from api.utils.views import GenericViewSet, error, success


# used for create or show user associated question
class QuestionViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin):

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
        else:
            question.is_watch = False
        ApiCli.process_question(question)
        seri = self.get_serializer(question)
        question.visit_count+=1
        question.save()
        return success(seri.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return success(data=serializer.data)
        key = list(serializer.errors.keys())[0]
        return error(key + ': ' + serializer.errors[key][0])

    def perform_create(self, serializer):
        question = serializer.save(author=self.request.user)
        profile = self.request.user.profile
        profile.watchedQuestion.add(question)
        profile.save()

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
                ApiCli.process_answer(answer, request.user)
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
    def watch(self, request, pk=None):
        if request.user.is_authenticated is False:
            return error('please login')
        question = self.get_object()
        if question is None:
            return error('question not exists')
        
        profile = request.user.profile
        Activity.watchQuestion(request.user.profile, question)

        profile.watchedQuestion.add(question)
        profile.save()
        return success()

    @detail_route(methods=['GET'],
                  permission_classes=[IsAuthenticated])
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
