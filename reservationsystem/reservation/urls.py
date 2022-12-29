from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ReservationsListView.as_view(), name="home"),
    path('register/', views.ReservationsCreateView.as_view(), name='create_reservation'),
    #path('validate_create_reservation', views.validate_create_reservation, name='validate_create_reservation'),
    path('create_rental/', views.RentalsCreateView.as_view(), name="create_rental"),
    #path('validate_create_rental', views.validate_create_rental, name="validate_create_rental")
]
   