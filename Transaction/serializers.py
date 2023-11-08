from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Transaction
from Toll.models import Toll
from User.models import Vehicle
from django.contrib.auth.models import User as DjangoUser
# Transaction Serializer

class TransactionSerializer(ModelSerializer):
    toll = serializers.PrimaryKeyRelatedField(queryset=Toll.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=DjangoUser.objects.all())
    vehicle_number = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    vehicle_distance = serializers.DecimalField(max_digits=10,decimal_places=2)
    transaction_time = serializers.DateTimeField()
    transaction_status = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ('user', 'toll', 'vehicle_number', 'vehicle_distance', 'transaction_time', 'transaction_status')

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)
    
    def validate (self, data):
        if data['transaction_status'] != 1:
            raise serializers.ValidationError("Transaction status must be 1")
        return data