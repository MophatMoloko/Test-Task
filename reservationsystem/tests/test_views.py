from django.test import TestCase, Client
from django.urls import reverse
from reservation.models import Rental, Reservations
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')


    def test_reservations_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/home.html')



