from rest_framework.permissions import IsAuthenticated

from api.models import Comment
from api.serializers import CommentSerializer, CommentCreateSerializer
from utils.views import GenericViewSet
from utils import mixins


class CommentsViewSet(GenericViewSet,
                      mixins.CreateModelMixin):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)