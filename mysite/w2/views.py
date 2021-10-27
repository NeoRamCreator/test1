from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import CreatePerson
from .models import *


def index(request):
    return render(request, 'w2/index.html', {})


# class PersonCreateView(CreateView):
#     # models = CreatePerson
#     # fields = ['title', 'text']
#     # fields = '__all__'
#     template_name = 'w2/index.html'
#     form_class = CreatePerson
#
#
# class PersonListenView(ListView):
#     model = Person
#     template_name = 'w2/index.html'


class All(CreateView, ListView):
    model = Person
    template_name = 'w2/index.html'
    form_class = CreatePerson
