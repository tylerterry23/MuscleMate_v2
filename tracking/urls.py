from django.urls import path
from .views import workout_index



urlpatterns = [
    path('workout/', workout_index, name='workout_index'),
]