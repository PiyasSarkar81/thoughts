from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:pk>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:pk>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
]