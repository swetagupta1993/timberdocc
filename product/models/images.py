from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=255, null=True)
    alt_tag = models.CharField(max_length=255, null=True)
    type_id = models.IntegerField(max_length=5, null=False, default=0)
    product_id = models.IntegerField(max_length=5, null=False, default=0)
