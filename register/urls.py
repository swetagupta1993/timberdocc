from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("register", views.Register.as_view(), name="register"),
    path("social_login", views.SocialLogin.as_view(), name="social"),
]
