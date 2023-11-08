from django.db import models
from django.contrib.auth.models import User as DjangoUser
from User.models import Vehicle
from Toll.models import Toll
from django.utils import timezone


#choices

STATUS_CHOICE = (
    (0,"Declined"),
    (1,"Processing"),
    (2,"Completed"),
)


class Transaction(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    toll  = models.ForeignKey(Toll, on_delete=models.CASCADE)
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_time = models.DateTimeField(default=timezone.now)
    transaction_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE,default=0)

    def __str__(self):
        return self.user.username + " , " + str(self.toll.id) + " , " + str(self.transaction_amount)

