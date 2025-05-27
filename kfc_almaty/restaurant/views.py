from django.shortcuts import render
from .models import Restaurant
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import Product

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'restaurant/index.html')

def menu_view(request):
    return render(request, 'restaurant/menu.html')

def payment(request):
    return render(request, 'restaurant/payment.html')

from django.shortcuts import render

def delivery(request):
    return render(request, 'restaurant/delivery.html')

def thankyou(request):
    return render(request, 'restaurant/thankyou.html')
