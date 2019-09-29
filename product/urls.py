from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeIndex.as_view(), name="product_index"),
    path("checkout", views.Checkout.as_view(), name="checkout"),
    path("single", views.Single.as_view(), name="single")
]