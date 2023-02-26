from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm


# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'username', 'email')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('email',)}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser'),
#         }),
#         # (_('Info'), {'fields': ('status',)}),
#     )
#
#
# admin.site.register(User, CustomUserAdmin)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """ Custom display user fields on admin panel"""

    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    ordering = ('email',)
    list_display = ('email', 'phone', 'is_staff', 'is_active',)
    list_filter = ('email', 'phone', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone', 'is_staff', 'is_active', 'lessons')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'phone', 'is_staff', 'is_active',),
            }
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.author_type = 'user'
        obj.author = str(request.user.id)
        obj.save()