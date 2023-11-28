from django.db import models

# Create your models here.

class Toll(models.Model):
    toll_name = models.CharField(max_length = 30)
    toll_location = models.CharField(max_length = 30)
    toll_charge_per_km = models.DecimalField(max_digits=10,decimal_places=2,default=100.00)
    toll_price_collected = models.DecimalField(max_digits=10,decimal_places=2,default=0.00) 

    def __str__(self):
        return str(self.id)

