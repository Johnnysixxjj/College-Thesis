from django.contrib import admin
from .models import Services, PetInfo, Appointment
# Register your models here.

admin.site.register(Services)
admin.site.register(PetInfo)
admin.site.register(Appointment)