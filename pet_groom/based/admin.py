from django.contrib import admin
from .models import ClientProfile, ServicesOffered, ClientAppointments, Invoices
# Register your models here.
admin.site.register(ServicesOffered)


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'l_name', 'phone_number', 'pet_name', 'pet_breed')


@admin.register(ClientAppointments)
class ClientAppointmentsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'full_name', 'contact_number', 'email_adress', 'appointment_date')
    