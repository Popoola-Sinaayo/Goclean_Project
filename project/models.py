from django.db import models
# Create your models here.


class User_Info(models.Model):
    name = models.CharField(max_length=1000, null=False, default="None")
    email = models.EmailField(default="None")
    pickup_address = models.CharField(max_length=1000, null=False)
    phone_number = models.IntegerField(default="+234", null=False)
    quantity_of_goods = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
