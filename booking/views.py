from django.shortcuts import render
from django.http import JsonResponse
from .models import Train, Booking
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.cache import cache

from django.http import JsonResponse
@csrf_exempt
def add_train(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', None)
        total_seats = data.get('total_seats', None)
        departure_time = data.get('departure_time', None)
        if not name:
            return JsonResponse({'error': 'Name field is required'}, status=400)
        try:
            train = Train.objects.create(name=name, total_seats=total_seats, departure_time=departure_time)
            return JsonResponse({'message': 'Train added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)


def view_trains(request):
    available_trains = cache.get('available_trains')
    if not available_trains:
        print("hi")
        available_trains = Train.objects.filter(total_seats__gt=0) #
        cache.set('available_trains', available_trains, 10)
    train_data = [{'name': train.name, 'total_seats': train.total_seats, 'departure_time': train.departure_time} for train in available_trains]
    return JsonResponse({'trains': train_data})


@csrf_exempt
def book_ticket(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        train_id = data.get('train_id', None)
        passenger_name = data.get('passenger_name', None)
        email = data.get('email', None)
        try:
            train = Train.objects.get(id=train_id)
            if train.total_seats > 0:
                seat_number = train.total_seats
                Booking.objects.create(train=train, passenger_name=passenger_name, seat_number=seat_number, email = email)
                train.total_seats -= 1
                train.save()
                return JsonResponse({'message': f'Ticket booked for {passenger_name} on train {train.name}',
                                     'seat_number': seat_number})
            else:
                return JsonResponse({'error': 'No seats available on this train'}, status=400)
        except Train.DoesNotExist:
            return JsonResponse({'error': 'Train not found'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

