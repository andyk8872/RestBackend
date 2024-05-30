from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView, posts_detail, PostsAPIView, postDetailsAPIView 

urlpatterns = [
    # path('posts/', PostView),
    # path('details/<int:pk>/', posts_detail),

    path('postsAPIView/', PostsAPIView.as_view()),
    path('detailsAPIView/<int:pk>/', postDetailsAPIView.as_view()),
]
