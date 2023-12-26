from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.TweetListView.as_view(),name='tweets'),
    path('user/regist/', views.UserRegistView.as_view(),name='usesr_regist'),
]