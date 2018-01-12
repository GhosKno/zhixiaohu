from rest_framework import serializers

from api.models import User, Profile, Topic, Question, Answer, Comment, Message, Activity


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user = User.objects.create(username=username, password=password, email=email)
        return user


class ResetPasswordSerializer(serializers.Serializer):
    old = serializers.CharField(max_length=50)
    new = serializers.CharField(max_length=50)


class AvatarSerializer(serializers.Serializer):
    file = serializers.ImageField(default='', )


class ProfileSerializer(serializers.ModelSerializer):
    is_watch = serializers.BooleanField(default=False)

    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'is_watch',
                  'nickname', 'description', 'watchCount',
                  'beWatchCount', 'answerCount')


class QuestionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'id', 'add_time', 'title',
                  'watch_count', 'answer_count')


# all url
# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('avatar', 'nickname', 'description', 'id')

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nickname', 'description')

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ProfileSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'nickname', 'description')


# class TopicCreateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Topic
#         fields = ('label', 'introduction', 'heat', 'questions')


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'label', 'introduction')


# # question will be send with detail
# class TopicDetailSerializer(serializers.HyperlinkedModelSerializer):
#     summaries = QuestionListSerializer(many=True)
#
#     class Meta:
#         model = Topic
#         fields = ('label', 'introduction', 'heat', 'summaries')


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'add_time', 'title', 'detail', 'topics', 'answer_count', 'watch_count')


class QuestionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title')


class AnswerSerializer(serializers.ModelSerializer):
    userSummary = ProfileSummarySerializer()
    comment_count = serializers.IntegerField()
    question = QuestionSummarySerializer()

    has_approve = serializers.BooleanField()
    has_against = serializers.BooleanField()
    has_favorite = serializers.BooleanField()

    class Meta:
        model = Answer
        fields = ('id', 'userSummary', 'approve', 'question', 'has_approve',
                  'has_against', 'has_favorite', 'add_time', 'detail', 'comment_count')


class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('detail',)


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('author', 'detail', 'question', 'id')
        read_only_fields = ('author', 'id')


class QuestionDetailSerializer(serializers.ModelSerializer):
    topics = TopicListSerializer(many=True)
    is_watch = serializers.BooleanField(default=False)

    class Meta:
        model = Question
        fields = ('author', 'id', 'add_time',
                  'watch_count', 'title', 'detail', 'topics',
                  'visit_count', 'is_watch', 'answer_count')


class CommentSerializer(serializers.ModelSerializer):
    userSummary = ProfileSummarySerializer()

    class Meta:
        model = Comment
        fields = ('id', 'detail', 'userSummary', 'add_time')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('answer', 'detail', 'add_time')


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    question = QuestionSummarySerializer()

    class Meta:
        model = Message
        fields = ('id', 'has_read', 'time', 'question', 'answer', 'author')


class ActivitySerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(allow_null=True)
    question = QuestionListSerializer(allow_null=True)
    watch = ProfileSerializer(allow_null=True)

    class Meta:
        model = Activity
        fields = ('answer', 'question', 'user',
                  'type', 'watch')
