from django.shortcuts import render, redirect # type: ignore
from .models import Table
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth import login # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import ReservationForm
from .models import Reservation
from django.shortcuts import get_object_or_404 # type: ignore


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
       return render(request, 'bookings/signup.html', {'form': form, 'errors': form.errors})
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

@login_required
def my_reservations(request):
  reservations = Reservation.objects.filter(user=request.user)
  return render(request, 'bookings/my_reservations.html', {'reservations': reservations})

@login_required
def delete_reservation(request, reservation_id):
  reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
  if request.method == 'POST':
       reservation.delete()
       return redirect('my_reservations')
  return render(request, 'bookings/confirm_delete.html', {'reservation': reservation})

@login_required
def edit_reservation(request, reservation_id):
  reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
  if request.method == 'POST':
     form = ReservationForm(request.POST, instance=reservation)
     if form.is_valid():
        form.save()
        return redirect('my_reservations')
  else: 
      form = ReservationForm(instance=reservation)
  return render(request, 'bookings/edit_reservation.html', {'form': form, 'reservation': reservation})    


