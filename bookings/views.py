from django.shortcuts import render, redirect
from .models import Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm


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

@login_required
def make_reservation(request):
  if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('home')
  else:
        form = ReservationForm()
  return render(request, 'bookings/make_reservation.html', {'form': form})

