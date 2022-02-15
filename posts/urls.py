from django.urls import path
from .views import (
    PostListView, 
    PostDetailedView, 
    PostCreateView
)


urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailedView.as_view(), name="post_detail"),
    path('posts/new/', PostCreateView.as_view(), name="post_new"),
]