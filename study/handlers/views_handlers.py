from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from study.models import Course
from .common_handlers import Queries


class ThemesHandler(Queries):

    def __init__(self, request: WSGIRequest, course_slug: str):
        self.request = request
        self.course_slug = course_slug
        self.user_id = request.user.id
        self.themes_data = {"themes": []}

    def get_themes(self) -> dict:
        """
        :return: dict
        {
            "themes": [
                {
                    "theme": Theme,
                    "is_open": bool,
                    "lessons": [
                                    {
                                        "lesson": Lesson,
                                        "is_open": bool
                                    },
                                ]
                },
            ]
        }
        """

        self._get_course()
        if self.request.user.is_superuser:
            self._get_themes_for_admin()
        else:
            self._get_themes_for_user()
        return self.themes_data

    def _get_course(self) -> None:
        self.themes_data['course'] = Course.objects.get(
            slug=self.course_slug,
        )

    def _get_themes_for_admin(self) -> None:
        course = self.themes_data['course']
        themes = self.get_themes_by_course(course=course)

        for theme in themes:
            lessons = []
            lessons_queryset = self.get_lessons_by_theme(theme=theme)
            for lesson in lessons_queryset:
                lessons.append(
                    {
                        "lesson": lesson,
                        "is_open": True,
                    }
                )
            self.themes_data['themes'].append(
                {
                    "theme": theme,
                    "is_open": True,
                    "lessons": lessons,
                }
            )

    def _get_themes_for_user(self) -> None:
        course = self.themes_data['course']
        user = self.get_user(user_id=self.user_id)
        themes = self.get_themes_by_course(course=course)
        opened_themes = [theme.id for theme in user.themes.all()]
        for theme in themes:
            lessons = []
            lessons_queryset = self.get_lessons_by_theme(theme=theme)
            opened_lessons = [lesson.id for lesson in user.lessons.all()]

            for lesson in lessons_queryset:
                lessons.append(
                    {
                        "lesson": lesson,
                        "is_open": True if lesson.id in opened_lessons else False
                    }
                )

            self.themes_data['themes'].append(
                {
                    "theme": theme,
                    "is_open": True if theme.id in opened_themes else False,
                    "lessons": lessons,
                }
            )


class TestsHandler(Queries):

    def __init__(self, request: WSGIRequest, lesson_id: int):
        self.request = request
        self.lesson_id = lesson_id
        self.user_id = request.user.id
        self.test_data = {}

    def get_questions(self) -> dict:
        self._complete_test_data()
        return self.test_data

    def _complete_test_data(self) -> None:
        test = self.get_test_by_lesson_id(lesson_id=self.lesson_id)
        if not test:
            raise Http404
        user = self.get_user(user_id=self.user_id)
        opened_lessons = [lesson.id for lesson in user.lessons.all()]
        self.check_permission(pk=self.lesson_id, access_pk_list=opened_lessons)
        self.test_data['test'] = test
        self.test_data['questions'] = self.get_questions_by_test(test=test)
