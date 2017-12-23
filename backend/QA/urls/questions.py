from django.urls import path, re_path
from QA.views import questions

urlpatterns = [
    re_path('^$', questions.PublishAPI.as_view()),
    path('<int:pk>/', questions.QuestionDetailAPI.as_view()),
    path('<int:topic_key>/<int:page>/<int: count>/',
         questions.QuestionAPI.as_view()),
    path('watch/', questions.QuestionWatchAPI.as_view()),
    path('cancel_watch/', questions.CancelWatchAPI.as_view()),
    path('search/<info>/<int:start>/<int:count>/',
         questions.QuestionSearchAPI.as_view())
]
