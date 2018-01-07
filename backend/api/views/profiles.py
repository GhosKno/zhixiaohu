from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route, detail_route
from rest_framework.parsers import MultiPartParser

from api.models import Profile
from api.serializers import ProfileSerializer, ProfileUpdateSerializer, AvatarSerializer, AnswerSerializer, \
    QuestionListSerializer, ProfileSummarySerializer

from utils.views import GenericViewSet, success, error
from utils import mixins


class ProfileViewSet(GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin):
    filter_backends = (SearchFilter,)
    search_fields = ('nickname',)

    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return ProfileUpdateSerializer
        if self.action == 'avatar':
            return AvatarSerializer
        return ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile:
            #watched = profile.user.watchedBy.all()
            #profile.watchedBy = watched
            seri = self.get_serializer(profile)
            return success(seri.data)
        return error("no profile found")

    # update nickname or description
    def partial_update(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile is None:
            return error("no profile found")
        data = request.data
        seri = self.get_serializer(data=data, partial=True)
        if seri.is_valid():
            seri.save(profile)
            return Response({'status': True})
        return Response(seri.errors)

    # upload avatar
    @list_route(methods=['POST'],
                parser_classes=(MultiPartParser,), )
    def avatar(self, request):
        seri = self.get_serializer(data=request.data)
        if seri.is_valid():
            avatar = seri.validated_data['file']
            profile = request.user.profile
            profile.avatar = avatar
            profile.save()
            return Response({'success': True})
        return Response({'success': False, 'msg': seri.errors})

    @detail_route(methods=['GET'])
    def favorites(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        answers = profile.favorites
        page = self.paginate_queryset(answers)
        if page is not None:
            for answer in page:
                profile = answer.author.profile
                answer.userSummary = profile
            serializer = AnswerSerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def questions(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        questions = profile.watchedQestion.all()
        page = self.paginate_queryset(questions)
        if page is not None:
            for answer in page:
                profile = answer.author.profile
                answer.userSummary = profile
            serializer = AnswerSerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def answers(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        answers = profile.agreed.all()
        page = self.paginate_queryset(answers)
        if page is not None:
            for answer in page:
                profile = answer.author.profile
                answer.userSummary = profile
            serializer = AnswerSerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def activities(self, request, pk=None):
        pass

    @detail_route(methods=['GET'])
    def watched_questions(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        questions = profile.watchedQuestion.all()
        page = self.paginate_queryset(questions)
        if page is not None:
            for question in page:
                question.answer_count = question.answers.count()
                question.watch_count = question.watchedUser.count()
            serializer = QuestionListSerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def watched_users(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        users = profile.watchedUser.all()
        profiles = users.first()
        for user in users[1:]:
            profiles |= user.profile
        page = self.paginate_queryset(profiles)
        if page is not None:
            serializer = ProfileSummarySerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def be_watched(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        profiles = profile.user.watchedBy.all()
        page = self.paginate_queryset(profiles)
        if page is not None:
            serializer = ProfileSummarySerializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')
