from django.urls import path
from . import views

urlpatterns = [
    path('laundry/booking', views.booking, name='neighbor_booking'),
    path('laundry/get_machine_availability/<str:machine_id>/', views.get_machine_availability, name='get_machine_availability'),
    ]
