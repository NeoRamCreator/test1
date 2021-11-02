from django.urls import path

from test1 import views

urlpatterns = [
    path('def/', views.image_upload_view),
    path('class/', views.Test1CreateView.as_view(), name='home'),
]
