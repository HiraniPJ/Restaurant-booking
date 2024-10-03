from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"
    
class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time}"
    