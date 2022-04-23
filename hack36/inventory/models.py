from django.db import models

class Inventory(models.Model):
    locationx = models.FloatField(default=0)
    locationy = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


# Create your models here.
