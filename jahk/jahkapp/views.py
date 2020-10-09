from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from dashboard.models import Course

def homepage(request):
    return render(request = request,
                  template_name='jahkapp/home.html',
                  context = {"event":Event.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "jahkapp/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "jahkapp/register.html",
                  context={"form":form})

class DashboardForm(ModelForm):
    class Meta:
        model = Course
        fields = ["intro", "duration", "points", "instructor"]
        labels = {
            "intro": "Introduction",
            "duration": "Duration (in seconds)",
            "points": "Points upon completion",
            "instructor": "Instructor"
        }


def dashboard(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}: {form.errors[msg]}")
    form = DashboardForm
    return render(request, "jahkapp/dashboard.html", {"form":form})
