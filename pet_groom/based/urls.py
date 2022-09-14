from django.urls import path
from . import views
from .views import CustomerProfilePage, update_customer_profile


urlpatterns = [
    path('', views.home_page, name='home'),
    path('customer-register', views.customer_register, name='customer-register'),
    path('customer-login', views.customer_login, name='customer-login'),
    path('customer-logout', views.customer_logout, name='customer-logout'),
    
    path('customer_profile/<int:pk>/', CustomerProfilePage.as_view(), name='customer-profile-page'),
    path('update_customer_profile/<int:id>/', views.update_customer_profile, name='update-customer-profile'),
    
    path('customer_appointment', views.create_customer_appointment, name='customer_appointment'),
    path('customer_appointment/<int:id>', views.customer_appointment_page, name='customer_appointment'),
    path('customer_appointment_update/<int:id>/', views.customer_appointment_update, name='customer_appointment_update'),
]
