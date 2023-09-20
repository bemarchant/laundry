from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.neighbor_login, name='neighbor_login'),
    path('signup/', views.neighbor_signup, name='neighbor_signup'),
    path('welcome/', views.neighbor_welcome, name='neighbor_welcome'),
]
