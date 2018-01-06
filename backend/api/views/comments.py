from api.models import Comment
from api.serializers import CommentSerializer, CommentCreateSerializer
from utils.views import GenericViewSet
from utils import mixins


class CommentsViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        #if self.action == 'create':
        return CommentCreateSerializer
        #return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


