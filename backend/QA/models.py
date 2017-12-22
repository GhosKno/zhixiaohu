from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    label = models.CharField(max_length=20)
    introduction = models.TextField()
    head = models.IntegerField(default=0)


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    title = models.CharField(u"标题", max_length=100)
    detail = models.TextField(u"描述")
    # watches in accounts
    topic = models.ManyToManyField(to=Topic, related_name='topic')


class Answer(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='answered',
                               )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # favitor agree disagree in accounts
    approve = models.IntegerField(u"赞同数", default=0)
    against = models.IntegerField(u"反对数", default=0)
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    detail = models.TextField(u"描述")




