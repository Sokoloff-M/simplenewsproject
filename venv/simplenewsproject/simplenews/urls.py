from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для списка новостей
    path('api/news/', views.NewsList.as_view(), name='news-list'),

    # Маршрут для отдельной новости по идентификатору
    path('api/news/<int:pk>/', views.NewsDetail.as_view(), name='news-detail'),

    # Маршрут для списка комментариев к новости
    path('api/news/<int:pk>/comments/', views.CommentList.as_view(), name='comment-list'),

    # Маршрут для отдельного комментария по идентификатору
    path('api/news/<int:pk>/comments/<int:comment_pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]
#