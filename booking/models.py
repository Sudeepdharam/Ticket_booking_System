from django.db import models
from django.utils import timezone


class Train(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField(default=0)
    departure_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.IntegerField()
    booking_time = models.DateTimeField(default=timezone.now)
    email = models.EmailField()

    def __str__(self):
        return f"{self.passenger_name} - {self.train.name}"
