from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.
# class Vehicle(models.Model):
#     user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
#     vehicle_number = models.CharField(max_length = 10,primary_key=True)
#     vehicle_type = models.CharField(max_length = 10)
#     vehicle_model = models.CharField(max_length = 10)
#     vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2,default=0)

#     def __str__(self):
#         return str(self.vehicle_number)