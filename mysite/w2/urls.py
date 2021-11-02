from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', PersonCreateView.as_view(), name='create_person_home'),

    path('list/', PersonListenView.as_view(), name='list_person'),

    # path('', All.as_view(), name='list_person'),

    # path('person/<int:pk>/', PersonCreateView.as_view(), name='people-detail'),

]
