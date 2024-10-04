from django.shortcuts import render
from .models import Table


# Create your views here.


def home(request):
  tables = Table.objects.all()
  return render(request, 'bookings/home.html', {'tables': tables})
