from django.db import models
from django.contrib.auth.models import User
# Create your models here



#front page models
class Services(models.Model):
    service_offered = models.CharField(max_length=100)
    service_description = models.TextField()
    service_price = models.CharField(max_length=10, default="Price For service")
    
    def __str__(self):
        return str(self.service_offered)
    
    
#after services
class CustomerInfo(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone_numb = models.CharField(max_length=11,null=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.l_name) 
    
class PetInfo(models.Model):
    owner = models.CharField(max_length=100)
    color = models.TextField()
    birthday = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.pet_name)
    
class Appointment(models.Model):
    owner = models.CharField(max_length=100)
    pet = models.CharField(max_length=100)
    services_available = models.ManyToManyField(Services)
    day_of_appointment = models.CharField(max_length=200)
    email = models.EmailField()
    appointment_confirmation = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.owner + self.pet)
