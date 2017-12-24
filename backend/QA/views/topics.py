from QA.models import Topic, TopicService

from QA.serializers.topics import TopicSerializer,TopicListSerializer
from utils import paged
from utils.views import APIView


class GetTopicsList(APIView):
    def get(self, req, page, counts):
        num = Topic.objects.count()
        page_handle = paged.page(num, page, counts)
        if not page_handle['valid']:
            return self.success([])
        topics = Topic.objects.all()[page_handle['start']:page_handle['end']]
        seri = TopicListSerializer(topics, many=True)
        return self.success(seri.data)


class GetTopicDetail(APIView):
    def get(self, req, id, page, counts):
        topic = TopicService.getTopicById(id)
        if not topic:
            return self.error('该话题不存在')
        num = topic.questions.count()
        page_handle = paged.page(num, page, counts)
        if not page_handle['valid']:
            return self.success([])
        questions = topic.questions.all()[page_handle['start']:page_handle['end']]
        topic['questions'] = questions
        seri = TopicSerializer(topic)
        return self.success(seri.data)


class GetHeatedTopicList(APIView):
    def get(self, req, page, counts):
        num = Topic.objects.count()
        page_handle = paged.page(num, page, counts)
        if not page_handle['valid']:
            return self.success([])
        topics = Topic.objects.order_by('heat')[page_handle['start']:page_handle['end']]
        seri = TopicListSerializer(topics, many=True)
        return self.success(seri.data)


class SearchTopic(APIView):
    def get(self, req, info, page, counts):
        topics = TopicService.searchTopicBlury(info)
        page_handle = paged.page(topics.count(), page, counts)
        if not page_handle['valid']:
            return self.success([])
        result = topics[page_handle['start']:page_handle['end']]
        seri = TopicSerializer(result, many=True)
        return self.success(seri.data)


class AddTopic(APIView):
    def post(self, req):
        data = req.data
        if not {'label', 'introduction'}.issubset(set(data.keys())):
            return self.error('bad params')

        topic = TopicService.addTopic(label=data['label'], introduction=data['introduction'], heat=0)

        if not topic:
            return self.error('话题已存在')

        return self.success(TopicSerializer(topic).data)
