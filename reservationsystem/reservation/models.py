from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Rental(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Reservations(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE, default='0')
    checkin = models.DateField()
    checkout = models.DateField()

def __str__(self):
    return f"Rental: {self.rental_id}, CheckIn: {self.checkin}, CheckOut: {self.checkout}"

