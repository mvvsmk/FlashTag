from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Transaction
from Toll.models import Toll
from User.models import Vehicle
from django.contrib.auth.models import User as DjangoUser
from User.models import Profile
from Toll.models import Toll
from django.utils import timezone

# Transaction Serializer

class TransactionSerializer(ModelSerializer):

    # user_no = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ['user','toll','vehicle_number','vehicle_distance','transaction_status','transaction_time']

    def validate(self, data): 
        print("---------------------------------")
        user = data['user']
        print(type(user))
        print(user)
        print("---------------------------------")
        toll = data['toll']
        print(type(toll))
        print(toll)
        print("---------------------------------")
        vehicle_number = data['vehicle_number']
        print(type(vehicle_number))
        print(vehicle_number)
        print("---------------------------------")
        vehicle_distance = data['vehicle_distance']
        print(type(vehicle_distance))
        print(vehicle_distance)
        print("---------------------------------")
        transaction_status = data['transaction_status']
        print(type(transaction_status))
        print(transaction_status)
        print("---------------------------------")


        # to check if all the data is valid

        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)  
        else:  
            raise serializers.ValidationError("Invalid User")


        if Vehicle.objects.filter(vehicle_number=vehicle_number).exists():
            vehicle = Vehicle.objects.get(vehicle_number=vehicle_number)
        else:
            raise serializers.ValidationError("Invalid Vehicle")


        # to process transaction
        transaction_amount = toll.toll_charge_per_km * vehicle_distance
        data['transaction_amount'] = transaction_amount
        
        transaction_time = timezone.now()
        data['transaction_time'] = transaction_time
        
        print(transaction_amount)

        if vehicle_distance < 0:
            transaction_status = 0
            data['transaction_status'] = transaction_status
            raise serializers.ValidationError("Vehicle distance cannot be negative")
        
        
        if transaction_amount < 0:
            transaction_status = 0
            data['transaction_status'] = transaction_status
            raise serializers.ValidationError("Transaction amount cannot be negative")
        
        
        if profile.account_balance < transaction_amount:
            transaction_status = 0
            data['transaction_status'] = transaction_status
            raise serializers.ValidationError("Insufficient balance")
        
        
        if vehicle.user != user:
            transaction_status = 0
            data['transaction_status'] = transaction_status
            raise serializers.ValidationError("Vehicle and User dont match")
        
        if transaction_status < 2:
            transaction_status = 2

        data['transaction_status'] = transaction_status

        # to save changes to database
        transaction = Transaction.objects.create(user=user,toll=toll,
                                                 vehicle_number=vehicle_number,
                                                 vehicle_distance=vehicle_distance,
                                                 transaction_amount=transaction_amount,
                                                 transaction_status=transaction_status,
                                                 transaction_time=transaction_time)
        return data