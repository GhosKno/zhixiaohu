from django.urls import include, path

from rest_framework.routers import DefaultRouter
from api.views import users, profiles, questions, topics, answers, comments, messages, images

route = DefaultRouter()
route.register('users', users.UserViewSet, base_name='user')
route.register('profiles', profiles.ProfileViewSet, base_name='profile')
route.register('questions', questions.QuestionViewSet, base_name='question')
route.register('topics', topics.TopicViewSet, base_name='topic')
route.register('answers', answers.AnswerViewSet, base_name='answer')
route.register('comments', comments.CommentsViewSet, base_name='comment')
route.register('messages', messages.MessageViewSet, base_name='message')

urlpatterns = [
    path('images/', images.ImageAPIView.as_view()),
    path('', include(route.urls))
]