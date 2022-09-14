from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ServicesOffered(models.Model):
    service_name = models.CharField(max_length=100)
    prices = models.DecimalField(max_digits=10, decimal_places = 2)
    service_description = models.TextField()
    
    def __str__(self):
        return str(self.service_name) + " php " + str(self.prices)



class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=12)
    home_address = models.CharField(max_length=100)
    
    pet_name = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=2)
    pet_breed = models.CharField(max_length=100, default="Put Breed Here")
    pet_name2 = models.CharField(max_length=50, blank=True, null = True)
    pet_age2 = models.CharField(max_length=2, blank=True, null = True)
    pet_breed2 = models.CharField(max_length=100, default="Put Breed Here")
    pet_name3 = models.CharField(max_length=50, blank=True, null = True)
    pet_age3 = models.CharField(max_length=2, blank=True, null = True)
    pet_breed3 = models.CharField(max_length=100, default="Put Breed Here")
    
    def __str__(self):
        return str(self.user) + " " + str(self.pet_name) + " " + str(self.pet_age)
    
    
class ClientAppointments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    email_adress = models.EmailField()
    
    service = models.ManyToManyField(ServicesOffered)
    appointment_date = models.CharField(max_length=9, default='m/d/y')
    time_of_day = models.CharField(max_length=10, default='00:00 pm/am') 

    appointment_finished = models.BooleanField(default=False)
    appointment_desc = models.TextField(default = 'Describe how the service went ', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

class Invoices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(ServicesOffered, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return str(self.user)
    
    