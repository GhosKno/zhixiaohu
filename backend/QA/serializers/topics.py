from rest_framework import serializers

from QA.models import Topic, Question



class TopicListSerializer(serializers.ModelSerializer):
    questions = Question.objects.count()

    class Meta:
        model = Topic
        exclude = ('questions')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'