from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from .forms import NeighborSignupForm, NeighborLoginForm


@csrf_protect

def neighbor_login(request):
    if request.method == 'POST':
        form = NeighborLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'login/welcome.html')
    else:
        form = NeighborLoginForm()

    return render(request, 'login/login.html', {'form': form})

def neighbor_logout(request):
    form = NeighborLoginForm()
    logout(request)
    
    return render(request, 'login/login.html', {'form': form})

def neighbor_signup(request):
    if request.method == 'POST':
        form = NeighborSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_superuser:
                print('superuser detected')
                return redirect('admin:index') 
            user.save()
            login(request, user)
            return neighbor_welcome(request)
        else:
            print('errors')
            print(form.errors)
            return render(request, 'login/signup.html', {'form': form})
    else:
        form = NeighborSignupForm()

    return render(request, 'login/signup.html', {'form': form})


def neighbor_welcome(request):
    print(request.user)
    return render(request, 'login/welcome.html')
