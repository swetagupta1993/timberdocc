from django.urls import path
from . import views

urlpatterns = [
    path("", views.Product.as_view(), name="admin_product"),
]
