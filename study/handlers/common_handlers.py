from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet
from user.models import User
from study.models import *



class Queries:

    @staticmethod
    def get_user(user_id: int) -> User:
        return User.objects.get(id=user_id)

    @staticmethod
    def get_themes_by_course(course: Course) -> QuerySet[Theme]:
        return Theme.objects.filter(
            course=course,
            is_hidden=False,
        ).order_by('priority')

    @staticmethod
    def get_lessons_by_theme(theme: Theme) -> QuerySet[Lesson]:
        return Lesson.objects.filter(
            theme=theme,
            is_hidden=False
        ).order_by('priority')

    @staticmethod
    def get_test_by_lesson_id(lesson_id: int) -> TestPart:
        return TestPart.objects.filter(
            lesson_id=lesson_id,
            is_hidden=False
        ).first()

    @staticmethod
    def get_questions_by_test(test: TestPart) -> QuerySet[Question]:
        return Question.objects.filter(
            test=test,
            is_hidden=False
        ).order_by('priority')

    @staticmethod
    def check_permission(pk: int, access_pk_list: list) -> None:
        if not pk in access_pk_list:
            raise PermissionDenied()