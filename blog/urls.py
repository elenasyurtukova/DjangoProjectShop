from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')
]