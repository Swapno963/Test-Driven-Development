from .views import register_user
from django.urls import path

urlpatterns = [
    path("signup/", register_user, name="signup_page"),
    ]
