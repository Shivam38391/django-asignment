from django.urls import path
from . import views


# app_name = 'acounts'

urlpatterns = [
    path('', views.index, name= "index"),
    path('register/', views.register, name= "register"),
    path('login/', views.login_view, name='login_view'),
    path('doctorpage/', views.doctor, name='doctorpage'),
    path('patientpage/', views.patient, name='patientpage'),
    
]
