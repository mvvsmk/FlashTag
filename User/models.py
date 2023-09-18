from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, primary_key=True)
    addhar_number = models.CharField(max_length = 12)
    phone_number = models.CharField(max_length = 10)
    account_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
# dummy data for class Profile in json format 
# {
#     "harit": {
#         "username": "harit",
#         "first_name": "Harit",
#         "last_name": "Mishra",
#         "email": "haritmishra@gmail",
#         "password": "harit123"
#          "addhar_number": "123456789012",
#          "phone_number": "1234567890",
#          "account_balance": 1000
#     },
#     "sarthak": {
#         "username": "sarthak",
#         "first_name": "Sarthak",
#         "last_name": "Mishra",
#         "email": "sarthakmishra@gmail",
#       "password": "sarthak123"
#          "addhar_number": "123456789012",
#          "phone_number": "1234567890",
#          "account_balance": 1000
#     },
#     "Aryan": {
#         "username": "Aryan",
#         "first_name": "Aryan",
#         "last_name": "Mishra",
#         "email": "aryanmishra@gmail",
#         "password": "aryan123"
#          "addhar_number": "123456789012",
#          "phone_number": "1234567890",
#          "account_balance": 1000
#     },

class Vehicles(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_number = models.CharField(max_length = 10)
    vehicle_type = models.CharField(max_length = 10)
    vehicle_model = models.CharField(max_length = 10)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.user.username + " " + self.vehicle_number

# dummy data for class Vehicles in json format
# {
#     "harit": {
#         "vehicle_number": "UP14AB1234",
#         "ve": "car",
#         "vehicle_type": "car",
#         "vehicle_model": "BMW",
#         "vehicle_distance": 1000
#     },