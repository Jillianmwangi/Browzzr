from django.urls import path
from .views import RegisterView, LoginView
from rest_framework import generics
from rest_framework.response import Response


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowUserView, UnfollowUserView

router = DefaultRouter()
router.register(r'users', generics, basename='user')

# urlpatterns = [
#     path('users/<int:pk>/follow/', FollowUnfollowView.as_view({'post': 'follow'}), name='follow-user'),
#     path('users/<int:pk>/unfollow/', FollowUnfollowView.as_view({'post': 'unfollow'}), name='unfollow-user'), 
#     path('', include(router.urls)),
# ]

# from .views import FollowView

# urlpatterns = [
#     path('follow/<int:user_id>/', FollowView.as_view()),
#     path('unfollow/<int:user_id>/', FollowView.as_view()),
# ]