
from django import forms
from dataclasses import fields
from .models import Reservations, Rental

class ReservationsForm(forms.ModelForm):

    class Meta:
        model = Reservations
        fields = "__all__"

class RentalsForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields ="__all__"