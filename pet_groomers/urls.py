from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='home'),
    
    path('register_customer/', views.register_customer, name='register_customer'),
    path('logout/', views.customer_logout, name='logout'),
    #spath('customer_profile/', views.customer_profile, name='customer_profile'),
    
    path('register_pet/', views.register_pet, name='register_pet'),
    
    path('appointment/', views.appointment_page, name='appointment'),

]
