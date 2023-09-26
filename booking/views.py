from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Machine, Booking
from datetime import date

def booking_status(request):
    today = date.today()
    pass

def booking(request):
    machine = Machine.objects.all()
    neighbor = request.user

    context = {'machine': machine, 'neighbor' : neighbor}

    if request.method == 'POST':
        selected_machine = Machine.objects.filter(name = request.POST.get('machine')).first()
        selected_slot = request.POST.get('slot')

        available_slots = selected_machine.get_slot_status()
        selected_machine.booked_slot(int(selected_slot))

        existing_booking = Booking.objects.filter(neighbor=request.user).first()
    
        if existing_booking:
            existing_booking.machine = selected_machine
            existing_booking.save()
        else:
            booking = Booking(neighbor=request.user, machine=selected_machine)
            booking.save()

        return render(request, 'booking/booking.html', context)
    
    return render(request, 'booking/booking.html', context)

def get_available_slots(request, machine_id):
    try:
        machine = Machine.objects.get(name=machine_id)
        slot_available = machine.get_slot_status()
        return JsonResponse({'slot_available': slot_available})
    
    except Machine.DoesNotExist:
        return JsonResponse({'error': 'Machine not found'})