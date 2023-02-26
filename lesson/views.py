from django.shortcuts import render
from django.views.generic import ListView
from user.models import User
from .models import Lesson


class MyLessons(ListView):

    model = User
    template_name = "lesson/my_lessons.html"
    context_object_name = "user_lessons"

    def get_queryset(self, **kwargs):
        if self.request.user.id:
            if self.request.user.is_superuser:
                context_object_name = "lessons"
                return Lesson.objects.all()
            return User.objects.get(id=int(self.request.user.id))


