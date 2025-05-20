from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.home),
    path('index.html', views.home, name='index.html'),
    path('hotel_view', views.home, name='hotel_view'),
]

