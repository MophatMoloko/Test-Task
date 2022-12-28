from django.contrib import admin
from . import models

# Register your models here.
myModels = [models.Reservations, models.Rental]

admin.site.register(myModels)