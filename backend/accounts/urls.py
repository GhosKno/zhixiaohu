from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('reset_password/', views.ResetPassWordAPI.as_view()),
    path('reset_nickname/', views.RestNickAPI.as_view()),
    path('profile/<int:pk>/', views.ProfileAPI.as_view()),
    path('likes/<int:pk>/<int:index>/<int:count>/',
         views.UserLikesAPI.as_view()),
    path('favorites/<int:pk>/<int:index>/<int:count>/',
         views.UserFavoritesAPI.as_view()),
    path('answers/<int:pk>/<int:index>/<int:count>/',
         views.UserAnsweredAPI.as_view()),
    path('history/<int:pk>/<int:index>/<int:count>/',
         views.UserHistoryAPI.as_view()),
    path('message/<int:pk>/',
         views.UserMessageAPI.as_view()),
    path('message_readed/<int:pk>/<int:msg_id>/',
         views.MessageAckAPI.as_view())
]