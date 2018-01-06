from rest_framework.decorators import detail_route

from api.models import Message
from utils.views import GenericViewSet, success, error


class MessageViewSet(GenericViewSet):
    queryset = Message.objects.all()

    @detail_route(methods=['GET'])
    def readed(self, request, pk=None):
        message = self.get_object()
        if message is None:
            return error('no message found')
        message.has_read = True
        message.save()
        return success()