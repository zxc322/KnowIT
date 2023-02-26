from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
