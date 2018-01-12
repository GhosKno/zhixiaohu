import random

from random_words import RandomNicknames

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UserManager(models.Manager):

    def create(self, username, password, email):
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        gender = random.choice('fmu')
        nickname = RandomNicknames().random_nick(gender=gender)
        profile = Profile(user=user, nickname=nickname)
        profile.save()
        return user

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=64, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Topic(models.Model):
    label = models.CharField(max_length=20, unique=True)
    introduction = models.TextField()
    heat = models.IntegerField(default=0)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'topic'
        ordering = ('-heat',)


class Question(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="published")
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    title = models.CharField(u"标题", max_length=100, unique=True)
    detail = models.TextField(u"描述")
    # watches in accounts
    topics = models.ManyToManyField(to=Topic, related_name='questions')
    visit_count = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'question'
        ordering = ('visit_count',)


class Answer(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='answered',
                               )
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    # favitor agree disagree in accounts
    approve = models.IntegerField(u"赞同数", default=0)
    against = models.IntegerField(u"反对数", default=0)
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    detail = models.TextField(u"描述")

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'answer'
        ordering = ('add_time',)


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='commented')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,
                               related_name='comments')
    detail = models.CharField(max_length=500)

    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'comment'
        ordering = ('add_time',)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='/static/avatar.jpg', upload_to='avatar')
    nickname = models.CharField(max_length=30)
    description = models.TextField(max_length=500)

    watchCount = models.IntegerField(default=0)
    beWatchCount = models.IntegerField(default=0)
    answerCount = models.IntegerField(default=0)

    watchedQuestion = models.ManyToManyField(to=Question, related_name='watchedUser')
    watchedUser = models.ManyToManyField(to=User, related_name='watchedBy')

    agreed = models.ManyToManyField(to=Answer, related_name='agreedUser')
    disagreed = models.ManyToManyField(to=Answer, related_name='disagreedUser')
    favorites = models.ManyToManyField(to=Answer)

    history = models.ManyToManyField(to=Question, related_name='history')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'profile'
        ordering = ('beWatchCount',)


class Message(models.Model):
    has_read = models.BooleanField(default=False)

    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='question')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, related_name='answer')
    time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'message'
        ordering = ('time',)


class Activity(models.Model):
    type = models.CharField(max_length=50)
    user = models.ForeignKey(to=Profile,
                             on_delete=models.CASCADE,
                             related_name='activities'
                             )
    # agree
    answer = models.ForeignKey(to=Answer,
                               on_delete=models.CASCADE,
                               null=True)
    # watch
    question = models.ForeignKey(to=Question,
                                 on_delete=models.CASCADE,
                                 null=True)
    # watch user
    watch = models.ForeignKey(to=Profile,
                              on_delete=models.CASCADE,
                              null=True)
    time = models.DateField(auto_now_add=True)

    @classmethod
    def watchQuestion(cls, user, question):
        cls.objects.create(type='QUES_WATCH',
                           question=question,
                           user=user).save()

    @classmethod
    def agreeAnswer(cls, user, answer):
        cls.objects.create(type='ANS_AGREE',
                           answer=answer,
                           user=user).save()

    @classmethod
    def watchUser(cls, user, watch):
        cls.objects.create(type='USER_WATCH',
                           watch=watch,
                           user=user).save()

    class Meta:
        db_table = 'activity'
        ordering = ('time',)
