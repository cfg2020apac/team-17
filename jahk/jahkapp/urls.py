from django.contrib import admin
from . import views
from django.urls import path, include

app_name = "jahkapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("/register", views.register, name="register"),
]
