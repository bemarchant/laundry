from django.urls import path
from . import views

urlpatterns = [
    path('laundry/booking/', views.booking, name='booking'),
    path('laundry/get_available_slots/<str:machine_id>/', views.get_available_slots, name='get_available_slots'),
    ]
