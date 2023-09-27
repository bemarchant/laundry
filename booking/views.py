from django.shortcuts import render, redirect
from django.http import JsonResponse
from login.views import neighbor_logout
from .models import Machine, Booking
from datetime import date

def booking_status(request):
    today = date.today()
    pass

def booking(request):
    machine = Machine.objects.all()
    neighbor = request.user
    existing_booking = Booking.objects.filter(neighbor=neighbor).first()

    context = {'machine': machine, 'neighbor' : neighbor, 'booking' : existing_booking}

    if request.method == 'POST':
        action = request.POST.get('action')
        
        machine_book =  existing_booking.machine
        slot_book = existing_booking.slot

        if action == 'book':
            selected_machine = Machine.objects.filter(name = request.POST.get('machine')).first()
            selected_slot = request.POST.get('slot')
        
            if existing_booking:
                selected_machine.booked_slot(int(selected_slot))
                selected_machine.booked_slot(int(slot_book))
                existing_booking.machine = selected_machine
                existing_booking.slot = selected_slot
                existing_booking.save()

            else:
                booking = Booking(neighbor=request.user, machine=selected_machine, slot = int(selected_slot))
                booking.save()
        
        if action == 'edit':
            print('edit')
        
        if action == 'cancel':
            machine_book.booked_slot(int(slot_book))
            existing_booking.slot = None
            existing_booking.machine = None
            existing_booking.save()

        if action == 'logout':
            return neighbor_logout(request)    
        
    return render(request, 'booking/booking.html', context)

def get_available_slots(request, machine_id):
    try:
        machine = Machine.objects.get(name=machine_id)
        slot_available = machine.get_slot_status()
        return JsonResponse({'slot_available': slot_available})
    
    except Machine.DoesNotExist:
        return JsonResponse({'error': 'Machine not found'})