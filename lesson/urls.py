from django.urls import path
from . import views

app_name = 'lesson'

urlpatterns = [
    path('', views.MyLessons.as_view(), name='my_lessons'),
]