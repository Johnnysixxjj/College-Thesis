from django import forms
from django.forms import ModelForm
from .models import ClientProfile, ClientAppointments


class ClientProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        fields = (
            'f_name', 
            'l_name', 
            'age', 
            'phone_number', 
            'home_address', 
            'pet_name', 
            'pet_age',
            'pet_breed',
            )

class ClientAppointmentForm(ModelForm):
    class Meta:
        model  = ClientAppointments
        fields = (
            'full_name',
            'contact_number',
            'email_adress',
            
            'service',
            'appointment_date',
        )