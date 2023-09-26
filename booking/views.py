from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Machine, Booking
from datetime import date

def booking_status(request):
    today = date.today()
    print(Booking.objects.count())
    pass

def booking(request):
    machine = Machine.objects.all()
    neighbor = request.user

    context = {'machine': machine, 'neighbor' : neighbor}

    if request.method == 'POST':
        selected_date = request.POST.get('date')
        selected_slot = request.POST.get('slot')

        if date.fromisoformat(selected_date) < date.today():
            return render(request, 'booking/booking.html', {'error_message': 'Selected date is in the past'})

        # Check if the selected slot is available for booking
        machine = Machine.objects.first()
        available_slots = machine.get_available_slots(selected_date)

        if selected_slot not in available_slots:
            return render(request, 'booking/booking.html', {'error_message': 'Selected slot is not available'})

        # Check if the slot is not already booked
        if Booking.objects.filter(machine=machine, date=selected_date, neighbor=request.user).exists():
            return render(request, 'booking/booking.html', {'error_message': 'You already have a booking for this slot'})

        # If all checks pass, create a booking
        booking = Booking(neighbor=request.user, machine=machine, date=selected_date)
        booking.save()
        return redirect('booking_success')  # Redirect to a success page

    return render(request, 'booking/booking.html', context)

def get_available_slots(request, machine_id):
    print(f' ######### machine selected : {machine_id}')
    try:
        machine = Machine.objects.get(name=machine_id)
        slot_available = machine.get_slot_status()
        return JsonResponse({'slot_available': slot_available})
    except Machine.DoesNotExist:
        return JsonResponse({'error': 'Machine not found'})