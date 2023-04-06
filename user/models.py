from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
)
from .managers import UserAccountManager
from study.models import Course, Theme, Lesson


class User(AbstractUser, PermissionsMixin):
    """ Custom User model """

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = UserAccountManager()

    username = None

    id = models.AutoField(
        primary_key=True,
        db_index=True,
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
    )
    email = models.EmailField(
        unique=True,
        db_index=True,
        verbose_name='email address',
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    courses = models.ManyToManyField(Course, related_name="courses", blank=True, default=None)
    themes = models.ManyToManyField(Theme, related_name="theme", blank=True, default=None)
    lessons = models.ManyToManyField(Lesson, related_name="lesson", blank=True, default=None)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        ordering = ['id']
