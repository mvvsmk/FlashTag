from django.db import models
from django.contrib.auth.models import User as DjangoUser
from User.models import Profile, Vehicle
from django.utils import timezone

# Create your models here.

class Toll(models.Model):
    toll_id = models.IntegerField(primary_key=True)
    toll_name = models.CharField(max_length = 30)
    toll_location = models.CharField(max_length = 30)
    toll_price_collected = models.DecimalField(max_digits=10,decimal_places=2) 

    def __str__(self):
        return self.toll_name

class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    toll_id = models.ForeignKey(Toll, on_delete=models.CASCADE)
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username 