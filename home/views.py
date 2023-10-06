from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .forms import NeighborSignupForm, NeighborLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test


@csrf_protect

def neighbor_login(request):
    if request.method == 'POST':
        print('neighbor_login')
        form = NeighborLoginForm(request.POST)

        if form.is_valid():
            print('form.is_valid()')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(f'{user} {username} {password}')
            if user is not None:
                login(request, user)
                return redirect('neighbor_welcome')
    else:
        form = NeighborLoginForm()

    return render(request, 'login.html', {'form': form})

def neighbor_logout(request):
    logout(request)
    return redirect('neighbor_login')

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
            return render(request, 'signup.html', {'form': form})
    else:
        form = NeighborSignupForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def neighbor_welcome(request):
    return render(request, 'welcome.html')

def is_super_neighbor(user):
    return user.groups.filter(name='Super Neighbor').exists()

@user_passes_test(is_super_neighbor)
def manage_apartments(request):
    # Your view logic for managing apartments here
    return