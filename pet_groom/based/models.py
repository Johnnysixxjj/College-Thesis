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
    phone_number = models.CharField(max_length=13)
    home_address = models.CharField(max_length=100)
    
    pet_name = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=2)
    pet_breed = models.CharField(max_length=100, default="Put Breed Here")
    
    
    def __str__(self):
        return str(self.user) + " " + str(self.pet_name) + " " + str(self.pet_age)
    
    
class ClientAppointments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email_adress = models.EmailField()
    
    service = models.ManyToManyField(ServicesOffered)
    appointment_date = models.DateField()
    time_of_day = models.TimeField()

    appointment_finished = models.BooleanField(default=False)
    appointment_desc = models.TextField(default = 'Describe how the service went ', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

class Invoices(models.Model):
    appointment_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    service = models.ForeignKey(ServicesOffered, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return str(self.appointment_user)
    
    