import uuid
from django.db import models
from django.contrib.auth.models import User as DjangoUser
from User.models import Vehicle,Profile
from Toll.models import Toll
from django.utils import timezone
from django.db.models.signals import(
    post_save,
)
from django.dispatch import receiver


#choices

STATUS_CHOICE = (
    (0,"Declined"),
    (1,"Processing"),
    (2,"Completed"),
)


class Transaction(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    toll  = models.ForeignKey(Toll, on_delete=models.CASCADE)
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_distance = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_time = models.DateTimeField(default=timezone.now)
    transaction_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE,default=0)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Transaction)
def update_toll_price_collected(sender, instance, created, **kwargs):
    if created:
        toll = instance.toll
        toll.toll_price_collected += instance.transaction_amount
        toll.save()
        vehicle = Vehicle.objects.get(vehicle_number=instance.vehicle_number)
        vehicle.vehicle_distance += instance.vehicle_distance
        vehicle.save()
        profile = Profile.objects.get(user=instance.user)
        profile.account_balance -= instance.transaction_amount
        profile.save()

