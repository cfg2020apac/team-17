from django.contrib import admin
from . import views
from django.urls import path, include

app_name = "jahkapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard")
    path("login", views.login_request, name="login"),
]
