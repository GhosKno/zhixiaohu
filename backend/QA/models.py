from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class Topic(models.Model):
    label = models.CharField(max_length=20)
    introduction = models.TextField()
    heat = models.IntegerField(default=0)


class TopicService(object):
    @staticmethod
    def exists(topic_label):
        num = Topic.objects.filter(label=topic_label).count()
        if num == 0:
            return False
        return True

    @staticmethod
    def getTopicById(id):
        try:
            topic = Topic.objects.get(id=id)
            return topic
        except Topic.DoesNotExist:
            return None

    @staticmethod
    def searchTopicBlury(info):
        topics = Topic.objects.filter(Q(label__icontains=info)|Q(introduction__icontains=info))
        return topics

    @staticmethod
    def addTopic(label, introduction, heat):
        if not TopicService.exists(label):
            topic = Topic.objects.create(label=label, introduction=introduction, heat=heat)
            topic.save()
            return topic
        return None

    @staticmethod
    def updateTopic(id, introduction):
        topic = TopicService.getTopicById(id)
        if topic:
            topic.introduction = introduction
            return True
        return False


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    title = models.CharField(u"标题", max_length=100)
    detail = models.TextField(u"描述")
    # watches in accounts
    topic = models.ManyToManyField(to=Topic, related_name='questions')


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


class AnswerService(object):
    @staticmethod
    def getAnswerByID(id):
        try:
            answer = Answer.objects.get(id=id)
            return answer
        except Answer.DoesNotExist:
            return None





