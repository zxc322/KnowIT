from django.db import models


class Lesson(models.Model):

    name = models.CharField(max_length=300)
    content = models.TextField(null=True, default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class UsersLessons(models.Model):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'user {self.user.id}, lesson {self.lesson.id}'



