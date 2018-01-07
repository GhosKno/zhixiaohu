from django.contrib import auth
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import User, Message
from api.serializers import LoginSerializer, RegisterSerializer, ResetPasswordSerializer, ProfileSerializer, \
    MessageSerializer
from utils.views import success, error


class UserViewSet(viewsets.GenericViewSet,
                  mixins.UpdateModelMixin):

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        if self.action == 'register':
            return RegisterSerializer
        if self.action == 'messages':
            return MessageSerializer
        return ResetPasswordSerializer

    def get_queryset(self):
        if self.action == 'messages':
            user = self.request.user
            return user.messages.all()
        return User.objects.all()

    @list_route(methods=['POST'],
                permission_classes=[])
    def login(self, request):
        data = request.data
        seri = self.get_serializer(data=data)
        if seri.is_valid():
            username = seri.validated_data['username']
            password = seri.validated_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                profile = user.profile
                seri = ProfileSerializer(profile , context={'request': request})
                return success(seri.data)
            return error('username or password not correct')
        return error(seri.errors)

    @list_route(methods=['GET'],
                permission_classes=(IsAuthenticated,))
    def logout(self, request):
        auth.logout(request)
        return success()

    @list_route(methods=['POST'],
                permission_classes=[])
    def register(self, request, *args, **kwargs):
        data = request.data
        seri = self.get_serializer(data=data)
        if not seri.is_valid():
            return Response(seri.errors)
        seri.save()
        username = seri.validated_data['username']
        user = User.objects.get(username=username)
        auth.login(request, user)
        profile = user.profile
        seri = ProfileSerializer(profile)
        return success(seri.data)

    def update(self, request, *args, **kwargs):
        seri = self.get_serializer(data=request.data)
        if not seri.is_valid():
            return Response({'status', False})
        user = request.user
        data = seri.validated_data
        if user.check_password(data['old']):
            user.set_password(data['new'])
            user.save()
            return Response({'status', True})
        return Response({'status', False})

    @list_route(methods=['GET'])
    def messages(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            temp = self.get_paginated_response(serializer.data)
            return success(temp.data)
        return error('no more message')

    @detail_route(methods=['GET'])
    def watch(self, request, pk=None):
        user = self.get_object()
        if user is None:
            return error('user not exists')
        profile = request.user.profile
        profile.watchedUser.add(user)
        profile.save()
        return success()

    @detail_route(methods=['GET'])
    def cancel_watch(self, request, pk=None):
        user = self.get_object()
        if user is None:
            return error('user not exists')
        profile = request.user.profile
        profile.watchedUser.remove(user)
        profile.save()
        return success()
