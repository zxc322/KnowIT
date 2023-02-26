from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
)
from .managers import UserAccountManager
from lesson.models import Lesson


class User(AbstractUser, PermissionsMixin):
    """ Custom User model """

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ["email"]
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
    
    lessons = models.ManyToManyField(Lesson, related_name="lessons", blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        ordering = ['id']
