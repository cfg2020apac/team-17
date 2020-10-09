from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.contrib.auth.forms import UserCreationForm

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
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "jahkapp/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "jahkapp/register.html",
                  context={"form":form})