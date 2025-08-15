from django.urls import path
from .views import register_view, tweet_create_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('create/', tweet_create_view, name='tweet_create'),
]