from django.urls import path
from QA.views import topics

urlpatterns = [
    path('', topics.AddTopic.as_view()),
    path('<int:page>/<int:counts>/', topics.GetTopicsList.as_view()),
    path('detail/<int:id>/<int:page>/<int:counts>/', topics.GetTopicDetail.as_view()),
    path('search/<info>/<int:page>/<int:counts>/', topics.SearchTopic.as_view()),
    path('heat/<int:page>/<int:counts>', topics.GetHeatedTopicList.as_view())
]
