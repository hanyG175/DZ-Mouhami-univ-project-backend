from django.db import models

from django.db import models
from django.utils import timezone
from phone_field import PhoneField


    
class Category(models.Model):
    name = models.CharField("Name", max_length=250)
    
    def __str__(self):
        return self.name

class Lawyer(models.Model):
    name = models.CharField("Name", max_length=240,default="N/A")
    photo = models.ImageField(upload_to='photos/',null=True)
    phone = models.CharField(null=True,max_length=20, default='N/A')
    email = models.EmailField(null=True,default='example@example.com')
    office_location = models.CharField(null=True,max_length=200, default='N/A')
    categories = models.ManyToManyField(Category, related_name='lawyers')  # ManyToManyField does not have a default option
    description = models.TextField(null=True,default='N/A')
    working_hours=  models.TextField(null=True,default='N/A')
    def __str__(self):
        return self.name
    
