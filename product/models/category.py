from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    level = models.IntegerField(max_length=2, blank=False, null=False, default=2)
    parent_id = models.IntegerField(max_length=5, null=False, default=0)
