from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, Home
from .models import User as users


@login_required
def home(request, template_name):
    if request.method == 'GET':
        form = Home
        # user = users.objects.filter()
    return render(request, 'registration/home.html', {'form': form})


def signup(request, template_name, next_page):
    # template_name = 'registration/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def edit(request,template_name):
    return render(request, 'registration/profile_edit.html')


def request(request, template_name):
    return render(request,'registration/request.html')
