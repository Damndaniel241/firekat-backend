from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass  

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="user_username")
    email = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="user_email")
    gender = models.CharField(max_length=8,blank=True,null=True)
    personal_text = models.CharField(max_length=50,blank=True,null=True)
    signature = models.CharField(max_length=50,blank=True,null=True)
    profile_picture = models.ImageField(upload_to='post_profiles/', null=True, blank=True)
    