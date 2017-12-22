from django.db import models
from django.contrib.auth.models import User

from QA.models import Question, Answer


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=30)
    description = models.TextField(max_length=500)

    watched_question = models.ManyToManyField(to=Question, blank=True, related_name='watchedQuestion')
    watched_user = models.ManyToManyField('self', blank=True)

    agreed_answer = models.ManyToManyField(to=Answer, blank=True, related_name='agreed')
    disagreed = models.ManyToManyField(to=Answer, blank=True, related_name='disagreed')
    favitor_answer = models.ManyToManyField(to=Answer, blank=True, related_name='favitor')

    history = models.ManyToManyField(to=Question, blank=True, related_name='history')


class Message(models.Model):
    has_read = models.BooleanField(default=False)

    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='receiver')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='question')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, related_name='answer')
    time = models.DateField(auto_created=True)


class UserService(object):
    @staticmethod
    def addUser(username, password, email):
        if not UserService.exists(username):
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        return None

    @staticmethod
    def deleteUser(id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False

    @staticmethod
    def updateEmail(id, email):
        user = UserService.getUserByID(id)
        if user:
            user.email = email
            user.save()
            return True
        return False

    @staticmethod
    def updatePassword(id, psd):
        user = UserService.getUserByID(id)
        if user:
            user.set_password(psd)
            user.save()
            return True
        return False

    @staticmethod
    def exists(username):
        num = User.objects.filter(username=username).count()
        if num == 0:
            return False
        return True

    @staticmethod
    def getUserByUserName(username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def getUserByID(id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def getUnreadMessage(user):
        set = Message.objects.filter(receiver=user)
        return set

    @staticmethod
    def processMessageAck(msg_id):
        try:
            msg = Message.objects.get(msg_id)
            msg.has_read = True
            return True
        except Message.DoesNotExist:
            return False

