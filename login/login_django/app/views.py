from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request, 'app/home.html')

@login_required
def products(request):
    return render(request, 'app/products.html')

def exit(request):
    return logout(request)

