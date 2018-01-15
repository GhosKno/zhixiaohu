from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Comment
from api.serializers import CommentSerializer, CommentCreateSerializer
from api.utils.views import GenericViewSet
from api.utils import mixins


class CommentsViewSet(GenericViewSet,
                      mixins.CreateModelMixin):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = self.perform_create(serializer)
        seri = CommentSerializer(comment, context={'request': request})
        headers = self.get_success_headers(seri.data)
        return Response({'success': True, 'data': seri.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        comment.userSummary = self.request.user.profile
        return comment

