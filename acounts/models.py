from django.db import models
from django.contrib.auth.models import AbstractUser
# from .manager import UserManager
# Create your models here.

class CustomUser(AbstractUser):
    
    # class Role(models.TextChoices):
    #     DOCTOR = "DOCTOR" , 'doctor'
    #     PATIENT= "PATIENT" , 'patient'
        
    # base_role = Role.DOCTOR
        
    
    image = models.ImageField(default= 'profilepic.jpg', upload_to= 'profile_pics')
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)

    # role = models.CharField(max_length=50, choices=Role.choices)
    is_doctor = models.BooleanField('Is Doctor', default=False)
    is_patient = models.BooleanField('Is Patient', default=False)
    
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #         return super().save(*args, **kwargs)


