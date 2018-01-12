from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated

from api.models import Message
from api.utils.views import GenericViewSet, success, error


class MessageViewSet(GenericViewSet):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated, )

    @detail_route(methods=['GET'])
    def readed(self, request, pk=None):
        message = self.get_object()
        if message is None:
            return error('no message found')
        message.has_read = True
        message.save()
        return success()

    @list_route(methods=['GET'])
    def unread(self, request):
        count = request.user\
            .messages.filter(has_read=False)\
            .count()
        return success({'count':count})

