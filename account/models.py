from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    FirstName = models.CharField(max_length=200, blank=True, null=True)
    LastName = models.CharField(max_length=200, blank=True, null=True)
    EmailAddress = models.EmailField(max_length=500, blank=True, null=True)
    #username = models.CharField(max_length=200, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=200, blank=True, null=True)
    
    #profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/img_avatar.png")
    Password = models.CharField(max_length=64, blank=True, null=True)
    ConfirmPassword = models.CharField(max_length=64, blank=True, null=True)
    
    


    def __str__(self):
        return str(self.FirstName )


