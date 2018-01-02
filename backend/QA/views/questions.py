from accounts.models import UserService
from utils.views import APIView
from QA.models import QAService
from QA.serializers.questions import QuestionSerializer


# TODO add auth and check params
class PublishAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'title', 'detail','topics'}\
                .issubset(set(data.keys())):
            return self.error('bad params')
        if QAService.existsQuestion(data['title']):
            return self.error('already exists')
        ques = QAService.addQuestion(data['title'],
                              data['detail'],
                              data['topics'],
                              request.user)
        seri = QuestionSerializer(ques)
        return self.success(seri.data)


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


class QuestionWatchAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        ques = QAService.getQuestionByID(data['question_id'])
        if ques is None:
            return self.error('no question found')

        user.profile.watchedQuestion.add(ques)
        return self.success()


class CancelWatchAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        ques = QAService.getQuestionByID(data['question_id'])
        if user is None or ques is None:
            return self.error('no question found')
        user.profile.watchedQuestion.remove(ques)
        return self.success()


class QuestionSearchAPI(APIView):
    def get(self, request, info, start, count):
        data = QAService.searchQuestion(info)
        data = data[start: start+count]
        seri = QuestionSerializer(data, many=True)
        return self.success(seri.data)

