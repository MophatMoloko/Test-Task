from django.shortcuts import render, redirect
from .models import Reservations, Rental
from .forms import ReservationsForm, RentalsForm
from django.views.generic import CreateView, ListView


# Create your views here.
class ReservationsListView(ListView):
    model = Rental
    context_object_name = 'zipped_reservations'
    template_name = 'reservation/home.html'

    def get_queryset(self):

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
        
        return zipped_reservations

        
class RentalsCreateView(CreateView):
    model = Rental
    success_url = '/reservation/create_rental/?status=0'
    form_class = RentalsForm

    def form_valid(self, form):

        self.object = form.save(commit=False)
        name = self.request.POST.get('name')

        if len(name.strip()) == 0:
            return redirect('/reservation/create_rental/?status=1')

        if Rental.objects.filter(name = name):
            return redirect('/reservation/create_rental/?status=2')
            
        try:
            rental = Rental(name = name)
            rental.save()
            self.object.save()
            return redirect(self.get_success_url())

        except:
            return redirect('/reservation/create_rental/?status=3')


class ReservationsCreateView(CreateView):
    model = Reservations
    success_url = '/reservation/home'
    form_class = ReservationsForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())