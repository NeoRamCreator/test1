from django.urls import path

from test1 import views

urlpatterns = [
    # path('def/', views.image_upload_view),

    path('class/', views.Test1CreateView.as_view(), name='home'),
    path('list2/', views.Test2ListView.as_view(), name='list2'),
    path('list1/', views.Test1ListView.as_view(), name='list1'),
    path('form/', views.Test1CreateView.as_view(), name='form'),
    # добавлен префикс _1 к именам
    path('list2/search/', views.Search.as_view(), name='search_1'),
    path('list2/filter/', views.Filter.as_view(), name='filter_1'),
]
