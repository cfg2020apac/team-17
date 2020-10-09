from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Event
from django.contrib import messages
from dashboard.models import Course
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

def homepage(request):
    return render(request = request,
                  template_name='jahkapp/home.html',
                  context = {"event":Event.objects.all})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "jahkapp/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("jahkapp:homepage")

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("jahkapp:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "jahkapp/register.html",
                          context={"form":form})

    form = NewUserForm
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
