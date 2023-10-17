from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from home.views import neighbor_logout
from .models import Machine, Booking
from datetime import datetime, timedelta, date
from django.utils import timezone

def booking_status(request):
    today = date.today()
    pass

@login_required

def booking(request):
    
    machines = Machine.objects.all()
    neighbor = request.user
    existing_booking = Booking.objects.filter(neighbor=neighbor).first()

    current_time = datetime.now()
    time_options = []

    context = {'machines': machines,
            'neighbor' : neighbor}
    
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'book':
            # machine_book =  existing_booking.machine
            # slot_book = existing_booking.slot
            selected_machine = Machine.objects.filter(name = request.POST.get('machine')).first()   
            selected_slot = request.POST.get('slot')

    #         if slot_book and machine_book:
    #             selected_machine.booked_slot(int(selected_slot))
    #             selected_machine.booked_slot(int(slot_book))
    #             existing_booking.machine = selected_machine
    #             existing_booking.slot = selected_slot
    #             existing_booking.save()

    #         elif existing_booking:
    #             booking = Booking(neighbor=request.user, machine=selected_machine, slot = int(selected_slot))
    #             booking.save()
    #             existing_booking.machine = selected_machine
    #             existing_booking.slot = selected_slot
    #             existing_booking.save()
            
    #         if not existing_booking:
    #             booking = Booking(neighbor=request.user, machine=selected_machine, slot = int(selected_slot))
    #             booking.save()
        
    #     if action == 'edit':
    #         print('edit')
        
    #     if action == 'cancel':
    #         print('cancel')
    #         print(machine_book)
    #         print(slot_book)
            
    #         if slot_book and machine_book:
    #             print('cancel')
    #             print(machine_book)
    #             print(slot_book)
    #             machine_book.booked_slot(int(slot_book))
    #             existing_booking.slot = None
    #             existing_booking.machine = None
    #             existing_booking.save()
        
        if action == 'logout':
            return neighbor_logout(request)    
        
    return render(request, 'booking.html', context)

@login_required

def get_machine_availability(request, machine_id):
    machine = Machine.objects.get(id=machine_id)
    available_slots = machine.slot_available()

    return JsonResponse({'slot_available': available_slots})