from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Person
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LogineUserForm(AuthenticationForm):
    class Mete:
        model = User
        fields = ['username', 'password']


class CreatePerson(ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'text', 'img']

        # widgets = {
        #     'text': Textarea(attrs={'cols': 30, 'rows': 5}),
        # }

        widgets = {
            'text': Textarea(attrs={
                'class': 't2',
                'cols': 28,
                'rows': 5,
            }),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
