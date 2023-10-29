from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, primary_key=True)
    addhar_number = models.CharField(max_length = 12,unique=True)
    phone_number = models.CharField(max_length = 10,unique=True)
    account_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_number = models.CharField(max_length = 10)
    vehicle_type = models.CharField(max_length = 10)
    vehicle_model = models.CharField(max_length = 10)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.user.username + " " + self.vehicle_number
