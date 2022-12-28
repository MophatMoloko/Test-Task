from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register, name='create_reservation'),
    path('validate_create_reservation', views.validate_create_reservation, name='validate_create_reservation'),
    path('create_rental/', views.create_rental, name="create_rental"),
    path('validate_create_rental', views.validate_create_rental, name="validate_create_rental")
]
   