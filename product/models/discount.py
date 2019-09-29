from django.db import models


class Discount(models.Model):
    product_id = models.IntegerField(max_length=5, null=False, default=0)
    type_id = models.IntegerField(max_length=5, null=False, default=0)
    type = models.CharField(max_length=255, null=True)
    disc = models.IntegerField(max_length=4, null=True)
    disc_price = models.IntegerField(max_length=5, null=True)
