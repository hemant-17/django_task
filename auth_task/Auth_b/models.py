from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    email=models.EmailField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    mobile_no = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.user}"