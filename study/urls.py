from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('courses/', views.Courses.as_view(), name='courses'),
    path('courses/<slug:slug>/', views.my_themes_view, name='themes'),
    path('test/<int:pk>/', views.lesson_test_view, name='test'),
    path('save_test_results/', views.save_test_results_ajax_view, name='save_test_results'),
]
