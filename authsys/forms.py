from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    def clean(self):
        res = super().clean()
        print(res)
        return res

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data.get('username'))
        except ObjectDoesNotExist:
            return self.cleaned_data.get('username')
        raise ValidationError('Пользователь с таким именем уже существует.')

    def validate_passwords(
        self,
        password1_field_name="password1",
        password2_field_name="password2",
    ):
        self.error_messages['password_mismatch'] = 'Пароли не совпадают'
        super().validate_passwords(password1_field_name, password2_field_name)

class SignInForm(AuthenticationForm):
    pass


