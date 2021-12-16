from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ImageForm
from .models import Test1, Test2


class Filter(ListView):
    template_name = 'test1/search.html'
    context_object_name = 'object_list'

    def get_queryset(self, **kwargs):
        get = super().get_context_data(**kwargs)
        get['title'].title = Test2.objects.order_by('title')
        return get


class Search(ListView):
    template_name = 'test1/search.html'
    context_object_name = 'object_list'

    # paginate_by = 4
    def get_queryset(self):
        return Test2.objects.filter(title__icontains=self.request.GET.get('s'))


class Test2ListView(ListView):
    model = Test2
    template_name = 'test1/list_view.html'
    success_url = reverse_lazy('home')


class Test1ListView(ListView):
    model = Test1
    template_name = 'test1/inc/_list.html'
    success_url = reverse_lazy('home')


class Test2CreateView(CreateView):
    model = Test2
    form_class = ImageForm
    template_name = 'test1/inc/_form.html'
    success_url = reverse_lazy('list2')


class Test1CreateView(CreateView):
    model = Test1
    form_class = ImageForm
    template_name = 'test1/index.html'
    success_url = reverse_lazy('list2')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['press'] = Test1.objects.all()
    #     return context

# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'test1/index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'test1/index.html', {'form': form})
