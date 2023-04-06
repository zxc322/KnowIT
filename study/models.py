from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings



class Course(models.Model):

    name = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField(null=True, blank=True, default=None)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Theme(models.Model):

    name = models.CharField(max_length=200)
    priority = models.SmallIntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} | {self.name}"


class Lesson(models.Model):

    name = models.CharField(max_length=200)
    priority = models.SmallIntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.theme.name} | {self.name}"


class TheoryPart(models.Model):

    text = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson.name


class CodePart(models.Model):

    description = models.CharField(max_length=300, null=True)
    code = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson.name


class TestPart(models.Model):

    title = models.CharField(max_length=300, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson.name


class Question(models.Model):

    question = models.CharField(max_length=500)
    test = models.ForeignKey(TestPart, on_delete=models.CASCADE)
    options = ArrayField(models.CharField(max_length=100))
    right_answer = models.CharField(max_length=100)
    priority = models.SmallIntegerField(default=0)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return F"test_id: {self.test.id} | {self.question}"


class UsersTestsResults(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(TestPart, on_delete=models.CASCADE)
    max_tries = models.SmallIntegerField(default=2)
    tries = models.SmallIntegerField(default=0)
    result = models.CharField(max_length=20)
    results_details = ArrayField(ArrayField(models.CharField(max_length=100)))

    def __str__(self):
        return F"User: {self.user.first_name} {self.user.last_name} | Test: {self.test}"