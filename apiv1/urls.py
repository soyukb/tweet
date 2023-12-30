from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('tweets/', views.TweetListView.as_view(),name='tweets'),
    path('user/regist/', views.UserRegistView.as_view(),name='usesr_regist'),
    path('api-token-auth/', auth_views.obtain_auth_token, name='obtain_auth_token'),
    # path('user/login/', views.UserLoginView.as_view(),name='usesr_login'),
]