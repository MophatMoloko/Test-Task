from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import ReservationsListView, RentalsCreateView,ReservationsCreateView

class TestUrls(SimpleTestCase):

    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class,ReservationsListView )

    def test_reservations_is_resolved(self):
        url = reverse('create_reservation')
        self.assertEquals(resolve(url).func.view_class, ReservationsCreateView )

    def test_rental_is_resolved(self):
        url = reverse('create_rental')
        self.assertEquals(resolve(url).func.view_class, RentalsCreateView )