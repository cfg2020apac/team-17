from django.contrib import admin
from . import views
from django.urls import path, include

app_name = "jahkapp"

urlpatterns = [
    path("", views.login_request, name="homepage"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("points/", views.rewards, name="points"),
    path("account/", views.account, name="account"),
]
