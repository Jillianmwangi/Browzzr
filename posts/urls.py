from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, like_post, unlike_post
from .views import FeedView
from django.urls import path


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    
    path('<int:pk>/like/', like_post.as_view, name='like_post'),
    path('<int:pk>/unlike/', unlike_post.as_view, name='unlike_post'),
]

