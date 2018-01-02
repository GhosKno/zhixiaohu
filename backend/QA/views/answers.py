from QA.models import QAService
from QA.serializers.answers import AnswerSerializer
from accounts.models import UserService
from utils.heat import HeatQueue
from utils.views import APIView
import threading


class AnswerAPI(APIView):
    def get(self, request, answer_id):
        answer = QAService.getAnswerByID(answer_id)
        if answer is None:
            return self.error('no answer found')
        seri = AnswerSerializer(answer)
        return self.success(seri.data)


class AnswerPulishAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'question_id', 'content'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        question = QAService.getQuestionByID(data['question_id'])
        if user is None or question is None:
            return self.error("cant\'t found user or question")
        content = data['content']
        answer = QAService.addAnswer(content, user, question)

        threading.Thread(target=msg_thread, args=(question, user, answer))

        seri = AnswerSerializer(answer)
        return self.success(seri.data)


class AnswerDeleteAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if answer is None:
            return self.error('no answer found')
        if answer.author is not user:
            return self.error('you have no permssion to do that')
        answer.delete()
        return self.success()


class FavoriteAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if answer is None:
            return self.error('no answer or user found')
        profile = user.profile
        profile.favitor_answer.add(answer)
        return self.success()


class CancelFavorAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if answer is None:
            return self.error('no answer or user found')
        profile = user.profile
        if profile.favitor_answer.filter(answer=answer).exists():
            profile.favitor_answer.remove(answer)
            return self.success()
        return self.error("you are not owner")


class AnswerLikeAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if answer is None:
            return self.error('no answer found')
        profile = user.profile
        profile.agreed_answer.add(answer)
        return self.success()


class CancelLikeAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        user = UserService.getUserByID(data['user_id'])
        answer = QAService.getAnswerByID(data['answer_id'])
        if user is None or answer is None:
            return self.error('no answer found')
        profile = user.profile
        if profile.agreed_answer.filter(answer=answer).exists():
            profile.agreed_answer.remove(answer)
            return self.success()
        return self.error("permission denied")


class AnswerDislikeAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if answer is None:
            return self.error('no answer found')
        profile = user.profile
        profile.disagreed.add(answer)
        return self.success()


class CancelDisLikeAPI(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return self.error("please login first")
        data = request.data
        if not {'user_id', 'answer_id'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        answer = QAService.getAnswerByID(data['answer_id'])
        if user is None or answer is None:
            return self.error('no answer found')
        profile = user.profile
        if profile.disagreed.filter(answer=answer).exists():
            profile.disagreed.remove(answer)
            return self.success()
        return self.error("no found")


def msg_thread(question, user, answer):
    q_users = question.watchedUser.all()
    u_users = user.WatchedBy.all()

    users = q_users | u_users  # merge
    for rec in users:
        UserService.addMessageForUser(rec, question, answer, user)

    for topic in question.topics:
        HeatQueue.put(topic)