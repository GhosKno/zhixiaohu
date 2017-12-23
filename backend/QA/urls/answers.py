from django.urls import path
from QA.views import answers

urlpatterns = [
    path('<int:answer_id>/', answers.AnswerAPI.as_view()),
    path('publish/', answers.PublishAPI.as_view()),
    path('delete/', ),
    path('favorite/', ),
    path('cancel_favorite/', ),
    path('like/', ),
    path('cancel_like/', ),
    path('dislike/', ),
    path('cancel_dislike/', )
]
