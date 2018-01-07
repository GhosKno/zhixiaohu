from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from api.models import Question
from api.serializers import QuestionCreateSerializer, QuestionDetailSerializer, AnswerSerializer
from utils.views import GenericViewSet, error, success


# used for create or show user assocatied question
class QuestionViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin):

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
        seri = self.get_serializer(question)
        return Response(seri.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route(methods=['GET'])
    def get_answers(self, request, pk):
        question = self.get_object()
        if question is None:
            return error("no topic found")

        queryset = self.filter_queryset(question.answers.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for answer in page:
                profile = answer.author.profile
                answer.userSummary = profile
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def watch(self, request, pk=None):
        question = self.get_object()
        if question is None:
            return error('question not exists')
        profile = request.user.profile
        profile.watchedQuestion.add(question)
        profile.save()
        return success()

    @detail_route(methods=['GET'])
    def cancel_watch(self, request, pk=None):
        question = self.get_object()
        if question is None:
            return error('question not exists')
        profile = request.user.profile
        profile.watchedQuestion.add(question)
        profile.save()
        return success()
