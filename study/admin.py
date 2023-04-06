from django.contrib import admin

from .models import Course, Theme, Lesson, TheoryPart, CodePart, TestPart, Question, UsersTestsResults


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Course._meta.fields]
    list_display_links = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Course


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Theme._meta.fields]
    list_display_links = ('name', 'id')

    class Meta:
        model = Theme


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Lesson._meta.fields]
    list_display_links = ('name', 'id')

    class Meta:
        model = Lesson


@admin.register(TheoryPart)
class TheoryPartAdmin(admin.ModelAdmin):

    list_display = [field.name for field in TheoryPart._meta.fields]
    list_display_links = ('lesson', 'id')

    class Meta:
        model = TheoryPart


@admin.register(CodePart)
class CodePartAdmin(admin.ModelAdmin):

    list_display = [field.name for field in CodePart._meta.fields]
    list_display_links = ('lesson', 'id')

    class Meta:
        model = CodePart


@admin.register(TestPart)
class TestPartAdmin(admin.ModelAdmin):

    list_display = [field.name for field in TestPart._meta.fields]
    list_display_links = ('lesson', 'id', 'title')

    class Meta:
        model = TestPart


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Question._meta.fields]
    list_display_links = ('id', 'question', 'test')

    class Meta:
        model = Question


@admin.register(UsersTestsResults)
class UsersTestsResultsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in UsersTestsResults._meta.fields]
    list_display_links = ('id', 'user', 'test')

    class Meta:
        model = UsersTestsResults
