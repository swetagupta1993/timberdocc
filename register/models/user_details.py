from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    mobile_number=models.BigIntegerField(blank=True, null=True)
    user_id=models.ForeignKey(to=User, on_delete=models.CASCADE)

