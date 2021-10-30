from django import forms
from django.forms import ModelForm, Textarea

from .models import Person


class CreatePerson(ModelForm):

    class Meta:
        model = Person
        fields = ['title', 'text', 'img']

        widgets = {
            'text': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
