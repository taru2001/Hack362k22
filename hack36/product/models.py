from django.db import models

# Create your models here.
from inventory.models import Inventory

class Product(models.Model):
    inventory = models.ForeignKey(Inventory , on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , default="")
    base_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=30,default="")
    description = models.CharField(max_length=50,default="")

    def __str__(self):
        return f'inventory: {self.inventory.id} {self.name}'

