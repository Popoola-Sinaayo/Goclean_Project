from django.db import models
import datetime
# Create your models here.


class User_Info(models.Model):
    name = models.CharField(max_length=1000, null=False, default="Not Supplied")
    email = models.EmailField(default="Not Supplied")
    pickup_address = models.CharField(max_length=1000, null=False)
    phone_number = models.CharField(max_length=30, default="Not Supplied")
    quantity_of_goods = models.IntegerField(default=0)
    time = models.CharField(max_length=1000, default=datetime.datetime.now())

    def __str__(self):
        return f"{self.name} ordered at {self.time}"
