from django.urls import path
from . import views

urlpatterns = [
    path('home/login', views.neighbor_login, name='neighbor_login'),
    path('home/signup', views.neighbor_signup, name='neighbor_signup'),
    path('home/welcome', views.neighbor_welcome, name='neighbor_welcome'),
]
