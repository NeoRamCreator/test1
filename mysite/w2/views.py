from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import CreatePerson
from .models import *


def index(request):
    return render(request, 'w2/index.html', {})


class PersonCreateView(CreateView):
    template_name = 'w2/index.html'
    form_class = CreatePerson
    success_url = reverse_lazy('create_person_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['press'] = Person.objects.all()
        return context


class PersonListenView(ListView):
    model = Person
    context_object_name = 'press'
    template_name = 'w2/_queryset.html'

# class All(CreateView, ListView):
#     model = Person
#     template_name = 'w2/index.html'
#     form_class = CreatePerson
