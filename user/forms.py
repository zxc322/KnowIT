from django import forms
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from .models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.template_name_label = ""

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'input-login-field'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'input-login-field'}))


class CustomUserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required fields """

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def clean_email(self):
        original_email = self.cleaned_data['email']

        # todo add validation if needed

        return original_email

    def save(
            self,
            commit=True,
    ):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(
            raw_password=self.cleaned_data["password1"],
        )

        if commit:
            user.save()

        return user


class CustomUserChangeForm(forms.ModelForm):
    """ A form for change new users. Includes all the required fields."""

    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            "using <a href=\"../password/\">this form</a>."
        )
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'phone',
            'is_staff',
            'is_active',
        )

    def clean_password(self):
        return self.initial["password"]

    def clean_email(self):
        original_email = self.cleaned_data['email']

        # todo add validation if needed

        return original_email
