from django.urls import path, re_path
from QA.views import questions

urlpatterns = [
    re_path('^$', questions.PublishAPI),
    path('<int:pk>/', questions.QuestionDetailAPI.as_view()),
    path('<int:topic_key>/<int:page>/<int: count>/',
         questions.QuestionAPI.as_view()),
    path('watch/', ),
    path('cancel_watch/', ),
    path('search/<info>/<int:start>/<int:count>/', ),
    path('page/<int:page>/counts-<int,default=20>/topic-<topic_key>/', )
]
