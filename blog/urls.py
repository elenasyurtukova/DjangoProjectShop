from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/list', PostListView.as_view(), name='posts_list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/create', ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete')
]