from accounts.models import UserService
from utils.views import APIView
from QA.models import QAService
from QA.serializers.questions import QuestionSerializer


# TODO add auth and check params
class PublishAPI(APIView):
    def post(self, request):
        data = request.data
<<<<<<< HEAD
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
=======
        seri = QuestionSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return self.success()
        return self.error(seri.error_messages)
>>>>>>> finished backend, ready for test


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
        data = request.data
        user = UserService.getUserByID(data['user_id'])
        ques = QAService.getQuestionByID(data['question_id'])
        if user is None or ques is None:
            return self.error('no user or question found')
<<<<<<< HEAD
        user.profile.watchedQuestion.add(ques)
=======
        user.profile.watched_question.add(ques)
>>>>>>> finished backend, ready for test
        return self.success()


class CancelWatchAPI(APIView):
    def post(self, request):
        data = request.data
        user = UserService.getUserByID(data['user_id'])
        ques = QAService.getQuestionByID(data['question_id'])
        if user is None or ques is None:
            return self.error('no user or question found')
<<<<<<< HEAD
        user.profile.watchedQuestion.remove(ques)
=======
        user.profile.watched_question.remove(ques)
>>>>>>> finished backend, ready for test
        return self.success()


class QuestionSearchAPI(APIView):
    def get(self, request, info, start, count):
        data = QAService.searchQuestion(info)
<<<<<<< HEAD
        data = data[start: start+count]
=======
>>>>>>> finished backend, ready for test
        seri = QuestionSerializer(data, many=True)
        return self.success(seri.data)

