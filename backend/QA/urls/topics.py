from django.urls import path
from QA.views import topics

urlpatterns = [
    path('/', topics.AddTopic.as_view()),
    path('<int:page>/<int:counts>/', topics.GetTopicsList.as_view()),
    path('detail/<int:id>/<int:page>/<int:count>/', topics.GetTopicDetail.as_view()),
    path('search/<str: info>/<int: page>/<int:counts>/', topics.SearchTopic.as_view())
]
