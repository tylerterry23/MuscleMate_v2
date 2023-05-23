from django.urls import path
from .views import social_feed



urlpatterns = [
    path('', social_feed, name='social_feed'),
]