from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=255, null=True)
    availability = models.BooleanField(null=False, default=1)
