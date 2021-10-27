from django import forms
from django.forms import ModelForm

from .models import Person


class CreatePerson(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
