from django.db import models
from django.utils import timezone 

class register(models.Model):
    Username=models.CharField(max_length=30)
    Email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    desig=models.CharField(max_length=13,default="user")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, default="General Inquiry")  # Default value for subject
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Default value for date and time

    def __str__(self):
        return self.name

