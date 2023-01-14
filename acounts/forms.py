from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )




class RegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username','image','address_line','state','pincode','city','email', "first_name", "last_name" ,'is_doctor','is_patient' )
        
        
