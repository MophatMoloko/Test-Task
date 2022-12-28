from django.shortcuts import render, redirect
from .models import Reservations, Rental
from .forms import ReservationsForm


# Create your views here.
def home(request):
    reservations_ordered = []
    previous_reservations = []
    rentals = Rental.objects.all()
    
    for rental in rentals:
        previous_reservation_id = '-'
        reservations = Reservations.objects.filter(rental_id=rental.id).order_by('checkin')

        for reservation in reservations:
            previous_reservations.append(previous_reservation_id)
            previous_reservation_id = reservation.id
            
        reservations_ordered.extend(reservations)
    zipped_reservations = zip(reservations_ordered, previous_reservations) 
        
    return render(request, 'reservation/home.html', {'zipped_reservations': zipped_reservations})


def create_rental(request):
    return render(request, 'reservation/create_rental.html')


def validate_create_rental(request):
    name = request.POST.get('name')

    if len(name.strip()) == 0:
        return redirect('/reservation/create_rental/?status=1')

    if Rental.objects.filter(name = name):
        return redirect('/reservation/create_rental/?status=2')
    
    try:
        rental = Rental(name = name)
        rental.save()

        return redirect('/reservation/create_rental/?status=0')

    except:
        return redirect('/reservation/create_rental/?status=3')



def register(request):
    form = ReservationsForm()
    return render(request, 'reservation/create_reservation.html', {'form': form})

def validate_create_reservation(request):
    form = ReservationsForm(request.POST)

    # TODO: validates the reservation interval
    if form.is_valid():
        form.save()
    return redirect('/reservation/home')
