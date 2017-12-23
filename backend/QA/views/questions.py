from utils.views import APIView
from QA.models import QAService
from QA.serializers.questions import QuestionSerializer


class PublishAPI(APIView):
    def post(self, request):
        data = request.data
        pass



class QuestionDetailAPI(APIView):
    def get(self, request, pk):
        question = QAService.getQuestionByID(pk)
        if question is None:
            return self.error('no question found')
        seri = QuestionSerializer(question)
        return self.success(seri.data)


class QuestionAPI(APIView):
    def get(self, request, topic_key, page, count):
        index = (page-1)*count
        topic = QAService.getTopicByID(topic_key)
        if topic is None:
            return self.error('can not found topic')
        data = topic.questions.all()[index:(index+count)]
        if data.exists():
            seri = QuestionSerializer(data, many=True)
            return self.success(seri.data)
        return self.error('no more data!')


class QuestionWathAPI(APIView):
    def post(self, request):
        pass

