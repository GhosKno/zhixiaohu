from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route, detail_route
from rest_framework.parsers import MultiPartParser

from api.models import Profile
from api.serializers import ProfileSerializer, ProfileUpdateSerializer, AvatarSerializer, AnswerSerializer, \
    QuestionListSerializer, ActivitySerializer

from utils.views import GenericViewSet, success, error
from utils import mixins


class ProfileViewSet(GenericViewSet,
                     mixins.RetrieveModelMixin):
    filter_backends = (SearchFilter,)
    search_fields = ('nickname',)

    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProfileSerializer
        if self.action == 'avatar':
            return AvatarSerializer
        if self.action == 'activities':
            return ActivitySerializer
        return ProfileUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile:
            if request.user.is_authenticated:
                count = request.user.profile\
                    .watchedUser.filter(profile=profile)
                profile.is_watch = count
            else:
                profile.is_watch = False
            seri = self.get_serializer(profile, context={'request':request})
            return success(seri.data)
        return error("no profile found")

    # update nickname or description
    @list_route(methods=['POST'],
                permission_classes=(IsAuthenticated, ))
    def update_info(self, request, *args, **kwargs):
        profile = self.request.user
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
        answers = profile.favorites.all()
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
        questions = profile.user.published.all()
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
    def answers(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        answers = profile.user.answered.all()
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
    def history(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error("no profile found")
        questions = profile.history.all()
        page = self.paginate_queryset(questions)
        if page is not None:
            for question in page:
                question.answer_count = question.answers.count()
                question.watch_count = question.watchedUser.count()
            serializer = QuestionListSerializer(page, many=True, context={'request': request})
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')


    @detail_route(methods=['GET'])
    def activities(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no such profile')
        activities = profile.activities.all()
        page = self.paginate_queryset(activities)
        if page is not None:

            for activity in page:
                if activity.watch:
                    activity.watch.is_watch=True
                elif activity.question:
                    activity.question.answer_count = \
                        activity.question.answers.count()
                    activity.question.watch_count = \
                        activity.question.watchedUser.count()
                elif activity.answer:
                    profile = activity.answer.author.profile
                    activity.answer.userSummary = profile

            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')


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
            serializer = QuestionListSerializer(page, many=True,
                                                context={'request': request})
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')

    @detail_route(methods=['GET'])
    def watched_users(self, request, pk=None):
        profile = self.get_object()
        if profile is None:
            return error('no profile found')
        users = profile.watchedUser.all()
        profiles = []
        for user in users:
            user.profile.is_watch = True
            profiles.append(user.profile)
        page = self.paginate_queryset(profiles)
        if page is not None:
            serializer = ProfileSerializer(page, many=True,
                                           context={'request': request})
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
            for profile in page:
                profile.is_watch = request.user.profile\
                    .watchedUser.filter(profile=profile).exists()
            serializer = ProfileSerializer(page, many=True,
                                           context={'request': request})
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more data')
