from django.shortcuts import render, redirect, get_object_or_404
from .models import Studio, Rent
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, RentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def studio_list(request):
    studios = Studio.objects.all()
    return render(request, 'list.html', {'studios': studios})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Аккаунт успешно создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, 'Вы больше не рэпер')
    return redirect('home')

@login_required
def profile(request):
    rents = Rent.objects.filter(user=request.user)
    return render(request, 'profile.html', {'rents': rents})

@login_required
def rent_studio(request, studio_id):
    studio = get_object_or_404(Studio, id=studio_id)
    if request.method == 'POST':
        form = RentForm(request.POST, user=request.user)
        if form.is_valid():
            rent = form.save(commit=False)
            rent.studio = studio
            rent.save()
            return redirect('profile')
    else:
        form = RentForm(user=request.user)
    return render(request, 'rent.html', {'form': form, 'studio': studio})

@login_required
def cancel_rent(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id, user=request.user)
    rent.delete()
    messages.success(request, 'Аренды больше нет...')
    return redirect('profile')

