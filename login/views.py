from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Neighbor, Apartment
from .forms import NeighborSignupForm

def neighbor_signup(request):
    if request.method == 'POST':
        form = NeighborSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or booking page after signup
    else:
        form = NeighborSignupForm()
    
    return render(request, 'login/signup.html', {'form': form})

