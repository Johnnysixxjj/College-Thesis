from django import forms
from .models import Services, CustomerInfo, PetInfo, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ["f_name", "l_name", 'phone_numb']
        
    def clean(self):
        
        super(CustomerForm, self).clean()
        
        f_name = self.cleaned_data.get('f_name')
        l_name = self.cleaned_data.get('l_name')
        phone_numb = self.cleaned_data.get('phone_numb')
        #email = self.cleaned_data.get('email')
        
        return self.cleaned_data
        
class PetForm(forms.ModelForm):
    class Meta:
        model = PetInfo
        fields =('owner','pet_name','pet_breed','color','birthday','gender')
    
        
        

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('owner', 'pet','services_available', 'day_of_appointment','email')
    