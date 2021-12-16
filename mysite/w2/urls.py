from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('mod_form', mod_form, name='mod_form'),
    # path('search/', views.search, name='search'),

    path('w2/', PersonCreateView.as_view(), name='create_person_home'),
    path('form/', PersonCreateViewForm.as_view(), name='form'),
    path('list/', PersonListenView.as_view(), name='list_person'),
    path('update/<int:pk>/', PersonUpdateView.as_view(), name='update'),
    path('w2/search/', views.Search.as_view(), name='search'),

    path('w2/filter/title/', views.FilterTitle.as_view(), name='filter_title'),
    path('w2/filter/price/', views.FilterPrice.as_view(), name='filter_price'),
    path('w2/filter/text/', views.FilterText.as_view(), name='filter_text'),
    path('w2/filter/id/', views.FilterId.as_view(), name='filter_id'),

]
