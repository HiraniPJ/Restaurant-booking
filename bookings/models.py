from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from cloudinary.models import CloudinaryField # type: ignore


# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=100, unique=True)
   # image = CloudinaryField('image')
    banner_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title    

    

class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time}"
    