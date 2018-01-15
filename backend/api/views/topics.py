from rest_framework.decorators import detail_route, list_route
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Topic
from api.serializers import TopicListSerializer, QuestionListSerializer, AnswerSerializer

from api.utils.views import error, success, GenericViewSet
from api.utils import mixins


class TopicSetPagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 10000


# create topic | list topic(search) | list question assocated with topic
class TopicViewSet(GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    filter_backends = (SearchFilter,)
    search_fields = ('label', 'introduction')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = TopicSetPagination

    def get_queryset(self, pk=None):
        return Topic.objects.all()

    def get_serializer_class(self):
        if self.action == 'get_questions':
            return QuestionListSerializer
        if self.action == 'get_answers':
            return AnswerSerializer
        return TopicListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return success(serializer.data)
        key = list(serializer.errors.keys())[0]
        return error(key + ': ' + serializer.errors[key][0])

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

    @list_route(methods=['GET'])
    def hot(self, request):
        topics = Topic.objects.order_by('-heat')[0:20]
        seri = self.get_serializer(topics, many=True)
        return success(seri.data)

    @detail_route(methods=['GET'])
    def get_answers(self, request, pk=None):
        topic = self.get_object()
        if topic is None:
            return error("no such a topic")
        questions = topic.questions.all()
        answers = []
        for question in questions:
            answer = question.answers.first()
            if answer is not None:
                answers.append(answer)

        page = self.paginate_queryset(answers)
        if page is not None:
            for instance in page:
                user = request.user
                if user.is_authenticated:
                    instance.has_approve = user.profile.agreed.filter(id=instance.id).exists()
                    instance.has_against = user.profile.disagreed.filter(id=instance.id).exists()
                    instance.has_favorite = user.profile.favorites.filter(id=instance.id).exists()
                else:
                    instance.has_approve = False
                    instance.has_against = False
                    instance.has_favorite = False
                instance.userSummary = instance.author.profile
                instance.comment_count = instance.comments.count()
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')
