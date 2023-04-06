from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from .models import Course
from .handlers.views_handlers import ThemesHandler, TestsHandler


class Courses(ListView):

    model = Course
    template_name = "study/courses.html"
    context_object_name = "courses"


def my_themes_view(request, slug: str):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('user:login'))
    context = dict()
    try:
        context['data'] = ThemesHandler(request=request, course_slug=slug).get_themes()
    except Exception:
        return render(request, 'base/error_page.html', context={"error": "Course doesn't exists"})

    return render(request, 'study/themes.html', context=context)


def lesson_test_view(request, pk: int):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('user:login'))
    context = dict()
    context['data'] = TestsHandler(request=request, lesson_id=int(pk)).get_questions()
    return render(request, 'study/tests.html', context=context)


def save_test_results_ajax_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('user:login'))
    if request.method == "POST":
        print('user_id', request.user.id)
        print("POST", request.POST)
        return JsonResponse({"response": "ZXC"})
