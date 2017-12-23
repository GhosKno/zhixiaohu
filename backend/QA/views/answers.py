from QA.models import AnswerService
from QA.serializers.answers import AnswerSerializer
from utils.views import APIView


class AnswerAPI(APIView):
    def get(self, request, answer_id):
        answer = AnswerService.getAnswerByID(answer_id)
        if answer is None:
            return self.error('no answer found')
        seri = AnswerSerializer(answer)
        return self.success(seri.data)


class PublishAPI(APIView):
    def post(self, request):
        pass

