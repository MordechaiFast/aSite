from django.shortcuts import render, redirect
from users.forms import UserCreationFormEMail
from django.contrib.auth import login
from django.urls import reverse

def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == "GET":
        return render(request, 'users/register.html',
         {'form': UserCreationFormEMail})
    elif request.method == "POST":
        form = UserCreationFormEMail(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
