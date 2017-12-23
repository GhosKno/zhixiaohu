from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q, QuerySet


class Topic(models.Model):
    label = models.CharField(max_length=20)
    introduction = models.TextField()
    heat = models.IntegerField(default=0)
    class Meta:
        db_table='topic'


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
    title = models.CharField(u"标题", max_length=100)
    detail = models.TextField(u"描述")
    # watches in accounts
    topics = models.ManyToManyField(to=Topic, related_name='questions')
    class Meta:
        db_table='question'


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
    class Meta:
        db_table='answer'


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
        topics = Topic.objects.filter(Q(label__icontains=info) | Q(introduction__icontains=info))
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


class QAService(object):
    @staticmethod
    def getAnswerByID(id):
        try:
            answer = Answer.objects.get(id=id)
            return answer
        except Answer.DoesNotExist:
            return None

    @staticmethod
    def getQuestionByID(id):
        try:
            q = Question.objects.get(id=id)
            return q
        except Question.DoesNotExist:
            return None

    @staticmethod
    def getTopicByID(id):
        try:
            topic = Topic.objects.get(id=id)
            return topic
        except Topic.DoesNotExist:
            return None

    @staticmethod
    def addAnswer(content, user, question):
        answer = Answer.objects\
            .create(author=user, question=question, detail=content)
        answer.save()
        return answer

    @staticmethod
    def searchQuestion(info):
        qlist = info.split(' ')
        res = set()
        for msg in qlist:
            temp = Question.objects.filter(title__contains=msg)
            res |= set(temp)
        res = list(res)
        return res

    @staticmethod
    def existsQuestion(title):
        return Question.objects.filter(title=title).exists()

    @staticmethod
    def addQuestion(title, detail, topics, user):
        ques = Question.objects.create(title=title,
                                detail=detail,
                                author=user)
        for id in topics:
            topic = TopicService.getTopicById(id=id)
            if topic is not None:
                ques.topics.add(topic)
            ques.save()
        return ques







