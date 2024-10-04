from django.shortcuts import render, redirect
from .models import Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.


def home(request):
  tables = Table.objects.all()
  return render(request, 'bookings/home.html', {'tables': tables})

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    
  else:
    form = UserCreationForm()
  return render(request, 'bookings/signup.html', {'form': form})
