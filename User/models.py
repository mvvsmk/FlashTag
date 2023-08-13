from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length = 30)
    addhar_number = models.CharField(max_length = 12)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 254)
    account_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Vehicles(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length = 10)
    vehicle_type = models.CharField(max_length = 10)
    vehicle_model = models.CharField(max_length = 10)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)


  