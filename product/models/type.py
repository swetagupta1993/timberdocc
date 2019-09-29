from django.db import models


class Type(models.Model):
    size = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    product_id = models.BigIntegerField(null=False, default=0)
    availability = models.BooleanField(null=False, default=1)
    price = models.FloatField(max_length=12, null=False, default=0.00)
    image = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(max_length=5, null=False, default=0)
