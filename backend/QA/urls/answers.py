from django.urls import path
from QA.views import answers

urlpatterns = [
    path('<int:answer_id>/', answers.AnswerAPI.as_view()),
    path('publish/', answers.AnswerPulishAPI.as_view()),
    path('delete/', answers.AnswerDeleteAPI.as_view()),
    path('favorite/', answers.FavoriteAPI.as_view()),
    path('cancel_favorite/', answers.CancelFavorAPI.as_view()),
    path('like/', answers.AnswerLikeAPI.as_view()),
    path('cancel_like/', answers.CancelLikeAPI.as_view()),
    path('dislike/', answers.AnswerDislikeAPI.as_view()),
    path('cancel_dislike/', answers.CancelLikeAPI.as_view())
]
