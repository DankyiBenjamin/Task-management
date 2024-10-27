from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

# register view


def home(request):
    return render(request, 'task/home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user immediately
            login(request, user)
            # redirect the user to the homepage
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'task/register.html', {'form': form})
