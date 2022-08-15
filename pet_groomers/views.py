from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Services, CustomerInfo, PetInfo, Appointment
from .forms import NewUserForm,CustomerForm, PetForm, AppointmentForm

# Create your views here.

def front_page(request):
    
    context = {}
    
    context['dataset'] = Services.objects.all()
    
    
    template_name = 'base.html'
    
    return render(request, template_name, context)
    


def register_customer(request):
    
        
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST['first_name']
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2:
            
            if User.objects.filter(username=username).exists():
                print('Username AlreadyExists')
                return redirect('register_customer')
            
            elif User.objects.filter(email=email).exists():
                print('Email Already Exists')
                return redirect('register_customer')
            
            print(username, email, first_name, last_name, password, password2)
            
            user = User.objects.create_user(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = password,
                )
            #user.save(commit=False)
            
            user.save()
            
            print(username, email, first_name, last_name, password, password2)

            login(request, user)
            print('successful registration')
            
            return redirect('register_pet')
            subject = "Welcome To the family"
            message = f"Hello {user.username}, thank you for registering"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            #send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Registration SuccessFul") 
            print('successful registration')
            
            return redirect('register_pet')
        
        else:
            print('Failed Registration')
            messages.error(request, "Unsuccessful registration")
            return redirect('register_customer')
            
            
    return render(request, 'register_customer.html')

"""
def customer_profile(request):
    
    if request.method == "POST":
        
        custom_form = CustomerForm(request.POST)
        if custom_form.is_valid():
            reg = custom_form.save(commit=False)
            
            reg.save()
            
            return redirect('pet_registration')
    
    else:
        custom_form = CustomerForm(None)
        return render(request, 'register_customer.html', {'form':custom_form})
        
    
    template_name = 'customer_profile.html'
    
    return render(request, template_name, {'form':custom_form})
"""


def register_pet(request):
    
    
    if request.method == "POST":
        pets_form = PetForm(request.POST)
        if pets_form.is_valid():
            pets_form.save(commit = False)
            pets_form.owner = request.user.username
            pets_form.save(commit=True)
            
            return redirect('home')
        
    else:
        print('form error')
        pets_forms= PetForm(request.POST)
        #return redirect('register-pet')
    
    pets_form = PetForm()
        
    template_name = 'pet_info.html'
    
    return render(request, template_name, {'form':pets_form})   



def appointment_page(request):
    
    if request.method == "POST":
        
        appointments = AppointmentForm(request.POST)
        if appointments.is_valid():
            obj = appointments.save(commit=False)
            obj.owner = request.user.username
            obj.save()
            print('appointment successful')

            return redirect('/')
        else:
            print('Failed')
            return redirect('appointment')
    appointments = AppointmentForm()

    
    template_name = 'customer_appointment.html'
    
    return render(request, template_name , {'form':AppointmentForm})