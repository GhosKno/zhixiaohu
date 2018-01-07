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


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    is_watch = serializers.BooleanField(default=False)

    class Meta:
        model = Profile
        fields = ('id', 'url', 'avatar', 'is_watch', 'nickname', 'description')


class QuestionListSerializer(serializers.HyperlinkedModelSerializer):
    answer_count = serializers.IntegerField()
    watch_count = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ('url', 'add_time', 'title', 'answer_count', 'watch_count')


# all url
# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('avatar', 'nickname', 'description', 'id')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', 'nickname', 'description')

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


#
class ProfileSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', 'nickname')


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
        fields = ('id', 'add_time', 'title', 'detail', 'topics')


class AnswerSerializer(serializers.ModelSerializer):
    userSummary = ProfileSerializer()
    comment_count = serializers.IntegerField(default=0)

    class Meta:
        model = Answer
        fields = ('userSummary', 'approve', 'question',
                  'add_time', 'detail', 'comment_count')


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('author', 'detail', 'question')
        read_only_fields = ('author',)


class QuestionDetailSerializer(serializers.ModelSerializer):
    topics = TopicListSerializer(many=True)
    is_watch = serializers.BooleanField(default=False)

    class Meta:
        model = Question
        fields = ('author', 'id', 'add_time',
                  'title', 'detail', 'topics',
                  'visit_count', 'is_watch')


class CommentSerializer(serializers.ModelSerializer):
    userSummary = ProfileSerializer()

    class Meta:
        model = Comment
        fields = ('detail', 'userSummary', 'add_time')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('detail', 'answer')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    question = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )

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
