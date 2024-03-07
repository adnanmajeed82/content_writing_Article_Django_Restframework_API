from django.urls import path
from .views import (
    WriterListCreateAPIView,
    WriterRetrieveUpdateDestroyAPIView,
    ArticleListCreateAPIView,
    ArticleRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('writers/', WriterListCreateAPIView.as_view(), name='writer-list-create'),
    path('writers/<int:pk>/', WriterRetrieveUpdateDestroyAPIView.as_view(), name='writer-retrieve-update-destroy'),
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-retrieve-update-destroy'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
]
