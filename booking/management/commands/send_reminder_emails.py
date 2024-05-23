import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from booking.models import Train, Booking

class Command(BaseCommand):
    help = 'Sends reminder emails to passengers of upcoming trains'

    def handle(self, *args, **options):
        current_time = datetime.datetime.now()
        thirty_minutes_from_now = current_time + datetime.timedelta(minutes=30)
        upcoming_trains = Train.objects.filter(departure_time__gt=current_time, departure_time__lte=thirty_minutes_from_now)
        for train in upcoming_trains:
            bookings = Booking.objects.filter(train=train)
            for booking in bookings:
                passenger_email = booking.email
                subject = "Reminder: Your Train Departure is Approaching"
                message = f"Dear Passenger,\n\nThis is a reminder that your train departure is approaching. 
                            Your seat details: {booking.seat_number}\n\nBest regards,\nThe Train Booking Team"
                send_mail(subject, message, 'your_email@example.com', [passenger_email])