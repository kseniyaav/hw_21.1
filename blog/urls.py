
from django.urls import path
from blog.apps import BlogConfig

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create_article'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_article'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_article'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_article'),
]