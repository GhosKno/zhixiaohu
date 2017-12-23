from django.contrib import auth

from utils.views import APIView

from accounts.models import UserService, Profile
from accounts.serializers import ProfileSerializer, MessageSerializer, UserSerializer


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        if not {'username', 'password', 'email'}.issubset(set(data.keys())):
            return self.error('bad params')

        user = UserService.addUser(username=data['username'],
                                   password=data['password'],
                                   email=data['email'])
        if user is not None:
            profile = Profile(user=user)
            profile.save()
            serializer = ProfileSerializer(profile)
            return self.success(serializer.data)
        else:
            return self.error('用户名已被使用')


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        if not {'username', 'password'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        name = data['username']
        psd = data['password']
        user = auth.authenticate(username=name, password=psd)
        if user:
            profile = user.profile
            seri = ProfileSerializer(profile)
            auth.login(request, user)
            return self.success(seri.data)
        return self.error('用户不存在or密码错误')


class ResetPassWordAPI(APIView):
    def post(self, request):
        data = request.data
        if not {'user_id', 'old_password', 'new_password'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        user = UserService.getUserByID(data['user_id'])
        if user and user.check_password(data['old_password']):
            user.set_password(data['new_password'])
            user.save()
            return self.success()
        return self.error('auth failed')


class RestNickAPI(APIView):
    def post(self, request):
        data = request.data
        if not {'user_id', 'new_nickname'} \
                .issubset(set(data.keys())):
            return self.error('参数错误')
        user = UserService.getUserByID(data['user_id'])
        # TODO add auth
        if user and user.is_authenticated:
            profile = user.profile
            profile.nickname = data['new_nickname']
            profile.save()
            return self.success()
        return self.error('auth failed')


class ProfileAPI(APIView):
    def get(self, request, pk):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('not found user')
        profile = user.profile
        seri = ProfileSerializer(profile)
        return self.success(seri.data)


# TODO serializer
class UserLikesAPI(APIView):
    def get(self, request, pk, index, count):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('not found user')
        profile = user.profile
        likes = profile.agreed.all()[index:(index + count)]
        if likes.exists():
            return self.success(likes)
        return self.error('no likes found')


class UserFavoritesAPI(APIView):
    def get(self, request, pk, index, count):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('not found user')
        profile = user.profile
        favorites = profile.favorites.all()[index:(index + count)]
        if favorites.exists():
            return self.success(favorites)
        return self.error('no favorites found')


class UserAnsweredAPI(APIView):
    def get(self, request, pk, index, count):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('not found user')
        answered = user.answered.all()[index, (index+count)]
        return self.success(answered)


class UserHistoryAPI(APIView):
    def get(self, request, pk, index, count):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('not found user')
        profile = user.profile
        history = profile.history.all()[index:(index + count)]
        if history.exists():
            return self.success(history)
        return self.error('no history found')


class UserMessageAPI(APIView):
    def get(self, request, pk):
        user = UserService.getUserByID(pk)
        if user is None:
            return self.error('no user found')
        msg = UserService.getUnreadMessage(user)
        seri = MessageSerializer(msg, many=True)
        return self.success(seri.data)


class MessageAckAPI(APIView):
    def get(self, request, pk, msg_id):
        if UserService.processMessageAck(msg_id):
            return self.success()
        return self.error('error when process ack')


class UserSearchAPI(APIView):
    def get(self, request, info):
        users = UserService.searchByName(info)
        seri = UserSerializer(users, many=True)
        return self.success(seri.data)


class WatchUserAPI(APIView):
    def get(self, request, id):
        user = UserService.getUserByID(id)
        if user is None:
            return self.error('no user found')
        me = request.user
        profile = me.profile
        profile.watchedUser.add(user)
        return self.success()