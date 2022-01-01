from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import message
from django.db.models import Q
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import CreatePerson, CreateUserForm, LogineUserForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


def loginPage(request):
    form = LogineUserForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_person_home')
    context = {'form': form, }
    return render(request, 'w2/auth/login.html', context)


def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'w2/auth/register.html', {'form': form})


def error(request):
    return render(request, 'w2/error.html', {})


def logoutUser(request):
    logout(request)
    return redirect('error')


# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Success! Add user: ' + user)
#             return redirect('login')
#         else:
#             messages.error(request, 'error! Add NOT user: ')
#     else:
#         form = CreateUserForm()
#     context = {'form': form}
#     return render(request, 'w2/auth/register.html', context)

#
# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('create_person_home')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Success! Add user: ' + user)
#                 return redirect('login')
#     context = {'form': form}
#     return render(request, 'w2/auth/register.html', context)
#

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
