from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Discount)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Images)
admin.site.register(models.Type)
