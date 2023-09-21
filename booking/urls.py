from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('booking/get_available_slots/<str:machine_id>/', views.get_available_slots, name='get_available_slots'),
    ]
