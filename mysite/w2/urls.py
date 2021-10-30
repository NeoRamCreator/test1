from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', PersonListenView.as_view(), name='list_person'),
    path('form/', PersonCreateView.as_view(), name='create_person'),


    # path('', All.as_view(), name='list_person'),

    # path('person/<int:pk>/', PersonCreateView.as_view(), name='people-detail'),

]
