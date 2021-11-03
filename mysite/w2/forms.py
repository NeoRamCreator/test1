from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Person


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

