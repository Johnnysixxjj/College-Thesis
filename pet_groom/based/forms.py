from django import forms
from django.forms import ModelForm
from .models import ClientProfile, ClientAppointments
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

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
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex: 0961999999'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'pet_breed': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ClientAppointmentForm(ModelForm):
    class Meta:
        model  = ClientAppointments
        fields = (
            'full_name',
            'contact_number',
            'email_adress',
            'appointment_date',
            'time_of_day',
            
            'service',
            'appointment_date',
        )
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_adress': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_date': DatePickerInput(),
            'time_of_day': TimePickerInput(),
            
            'service': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }