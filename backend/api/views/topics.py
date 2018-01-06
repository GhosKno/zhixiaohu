from rest_framework.decorators import detail_route, list_route
from rest_framework.filters import SearchFilter

from api.models import Topic, Question
from api.serializers import TopicListSerializer, QuestionListSerializer

from utils.views import error, success, GenericViewSet
from utils import mixins


# create topic | list topic(search) | list question assocated with topic
class TopicViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):

    filter_backends = (SearchFilter, )
    search_fields =('label', 'introduction')

    def get_queryset(self, pk=None):
        return Topic.objects.all()

    def get_serializer_class(self):
        if self.action == 'get_questions':
            return QuestionListSerializer
        return TopicListSerializer

    @detail_route(methods=['GET'])
    def get_questions(self, request, pk=None):
        topic = self.get_object()
        if topic is None:
            return error("no topic found")

        queryset = self.filter_queryset(topic.questions.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            for question in page:
                question.answer_count = question.answers.count()
                question.watch_count = question.watchedUser.count()
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    # TODO
    @detail_route(methods=['GET'])
    def get_answers(self, request, pk=None):
        pass

    @list_route(methods=['GET'])
    def hot(self, request):
        topics = Topic.objects.order_by('-heat')[0:20]
        seri = self.get_serializer(topics, many=True)
        return success(seri.data)






