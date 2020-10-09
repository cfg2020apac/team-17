from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request = request,
                  template_name='jahkapp/home.html',
                  context = {"event":Event.objects.all})

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "jahkapp/register.html",
                  context={"form":form})