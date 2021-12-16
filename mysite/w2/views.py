from django.core.mail import message
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import CreatePerson
from .models import *


class Search(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'press'

    def get_queryset(self):
        return Person.objects.filter(title__icontains=self.request.GET.get('s'))


class FilterTitle(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all().order_by('title')
        return queryset


class FilterPrice(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all().order_by('price')
        return queryset


class FilterText(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all().order_by('text')
        return queryset


class FilterId(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all().order_by('-id')
        return queryset


class FilterText(ListView):
    template_name = 'w2/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Person.objects.all().order_by('text')
        return queryset


class PersonCreateView(CreateView):
    template_name = 'w2/index.html'
    form_class = CreatePerson
    success_url = reverse_lazy('create_person_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Person.objects.all()
        return context


class PersonCreateViewForm(CreateView):
    template_name = 'w2/form1.html'
    form_class = CreatePerson
    success_url = reverse_lazy('create_person_home')


class PersonListenView(ListView):
    model = Person
    context_object_name = 'press'
    template_name = 'w2/_queryset.html'


class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'w2/form1.html'
    form_class = CreatePerson
    success_url = reverse_lazy('create_person_home')

# class All(CreateView, ListView):
#     model = Person
#     template_name = 'w2/index.html'
#     form_class = CreatePerson
# def search(request):
#     if request.metod == 'get':
#         srch = request.POST['srh']
#         if srch:
#             match = Person.object.filter(
#                 Q(title__icontains=srch) |
#                 Q(text__icontains=srch)
#             )
#             if match:
#                 return render(request, 'w2/index.html', {'sr': match})
#             else:
#                 message.error(request, 'no result found')
#         else:
#             return HttpResponseRedirect('/create_person_hom/')
#     return render(request, 'w2/index.html')

# def get_queryset(self):
#     name = self.kwargs.get('q', '')
#     object_list = self.model.objects.all()
#     if name:
#         object_list = object_list.filter(name__icontains=name)
#     return object_list

# def get_queryset(self):  # новый
#     query = self.request.GET.get('q')
#     object_list = Person.objects.filter(
#         Q(name__icontains=query) | Q(state__icontains=query)
#     )
#     return object_list
# class PersonUpdateView(UpdateView):
#     model = Person
#     fields = ['title', 'text', 'img']
#     template_name = 'w2/form1.html'
#     success_url = reverse_lazy('create_person_home')
#     form_class = CreatePerson

# def search(request):
#     if request.metod == 'POST':
#         srch = request.POST['srh']
#         if srch:
#             match = Person.object.filter(
#                 Q(title__icontains=srch) |
#                 Q(text__icontains=srch)
#             )
#             if match:
#                 return render(request, 'w2/index.html', {'sr':match})
#             else:
#                 message.error(request, 'no result found')
#         else:
#             return HttpResponseRedirect('/create_person_hom/')
#     return render(request, 'w2/index.html')
# def index(request):
#     return render(request, 'w2/index.html', {})


# def mod_form(request):
#     return render(request, 'w2/_mod_window.html', {})
