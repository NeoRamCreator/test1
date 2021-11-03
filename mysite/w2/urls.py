from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),

    path('', PersonCreateView.as_view(), name='create_person_home'),
    path('form/', PersonCreateViewForm.as_view(), name='form'),
    path('list/', PersonListenView.as_view(), name='list_person'),
    path('update/<int:pk>/', PersonUpdateView.as_view(), name='update'),

]
