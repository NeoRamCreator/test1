from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import CreatePerson
from .models import *


def index(request):


    return render(request, 'w2/index.html', {})


class PersonCreateView(CreateView):
    template_name = 'w2/index.html'
    form_class = CreatePerson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['press'] = Person.objects.all()
        return context


class PersonListenView(ListView):
    model = Person
    template_name = 'w2/index.html'




# class All(CreateView, ListView):
#     model = Person
#     template_name = 'w2/index.html'
#     form_class = CreatePerson
