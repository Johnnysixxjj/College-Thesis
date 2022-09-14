from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from django.views.generic.edit import FormView, CreateView

from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User

from django.conf import settings

from django.urls import reverse_lazy
from .models import ServicesOffered, ClientProfile, ClientAppointments
from .forms import ClientProfileForm, ClientAppointmentForm
# Create your views here.


class CustomerProfilePage(DetailView):
    model = ClientProfile
    template_name = 'client_profile.html'
    user = ClientProfile.objects.all()
    def get_context_data(self, *args, **kwargs):
        
        context = super(CustomerProfilePage, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(ClientProfile, id=self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context
        return render(request, template_name, context)
        
def update_customer_profile(request, id):
    context = {}
    obj = get_object_or_404(ClientProfile, id=id)
    form = ClientProfileForm(request.POST or None, instance = obj)
    if request.method == "POST":

        if form.is_valid():
            obj.save()
            messages.success(request,'Updated your profile')
            return redirect('/')
        
        else: 
            messages.error(request, "There was an error")
            return redirect('update_customer_profile')
        
    context['form'] = form
    context['obj'] = obj
    return render(request, 'create_customer_profile.html', context)
            
    
        

def home_page(request):
    
    context = {}
    
    context['appointments'] = ClientAppointments.objects.all()
    
    context['dataset'] = ServicesOffered.objects.all()
    
    template_name = 'base.html'
    
    return render(request, template_name, context)

def customer_logout(request):
    logout(request)
    return redirect('/')

def customer_register(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2 :
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Already in use")
                return redirect('customer-register')

            user = User.objects.create_user(
                username = username,
                password = password,
            )
            ClientProfile.objects.update_or_create(
                user=user
            )
            user.save()
            
            messages.success(request, "Account Created, Click on the Edit Document above to add some information about you and your pet")
            login(request, user)
            return redirect('/')
        
        else:
            return redirect('customer-register')
            return render(request, 'register_customer.html')
        
    return render(request, 'register_customer.html')

def customer_login(request):
    
    if request.method == "POST":
    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            messages.success(request, 'Login Success')
            return redirect('/')
        else:
            messages.info(request, 'Login Error')
            return render(request, 'login.html')

    
    return render(request, 'login.html')

def create_customer_appointment(request):
    context = {}
    context['appointments'] = ClientAppointments.objects.all()
    form = ClientAppointmentForm(request.POST or None)
    if request.method == 'POST':
        form = ClientAppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            
            subject = "Appointment Conformation"
            message = f"Hello {request.user} This is an email Confirming your appointment time at {appointment.appointment_date}, We hope to see you there!"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [appointment.email_adress,]
            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, 'Form was accepted')
            return redirect('/')
        else:
            messages.error(request, "An error occured")
            return redirect('customer_appointment')
    context['appointments'] = ClientAppointments.objects.all()
    context['form'] = form
    return render(request, 'client_appointment_create.html', context)

def customer_appointment_update(request, id):
    context = {}
    
    obj = get_object_or_404(ClientAppointments, id=id)
    form = AppointmentForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        form.save()
        
        
        return redirect('/')
    
    context['form'] = form
    
    return render(request, 'customer_appointment_update.html', context)

def customer_appointment_page(request, id):
    context = {}
    
    context['data'] = ClientAppointments.objects.get(id=id)
    
    return render(request, 'appointment_page.html', context)
    
def create_invoice(request):
    pass