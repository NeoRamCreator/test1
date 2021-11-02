from django import forms
from .models import Test1


class ImageForm(forms.ModelForm):
    class Meta:
        model = Test1
        fields = ('title', 'img')