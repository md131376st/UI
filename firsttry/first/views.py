from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, Home, RequestForm , LoginForm
# import first.forms as form_
# from firsttry.settings import AUTHENTICATION_BACKENDS
#
# from django.contrib.auth import views as auth_views
# from  django.contrib.auth.forms import AuthenticationForm
# from .models import User as users


@login_required
def home(request, template_name):
    if request.method == 'GET':
        form = Home(request.GET)
        # user = users.objects.filter()
    return render(request, 'registration/home.html', {'form': form})


def signup(request, template_name, next_page):
    # template_name = 'registration/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # username = form.cleaned_data.get('email')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def edit(request,template_name):
    return render(request, 'registration/profile_edit.html')


def request(request, template_name, next_page):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RequestForm(request.POST)
            form.save()
        else:
            form = RequestForm()
        return render(request, 'registration/request.html', {'form': form})


def requestdone(request,template_name):
    return render(request, 'registration/requestdone.html')


# def login_(request,template_name):
#     # form = csrf(request)
#     # auth_views.login()
#     print("life")
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print("me")
#         print(form.cleaned_data.get('email'))
#         print (form.is_valid())
#         if form.is_valid():
#             print("hi")
#             login(request, form)
#             return redirect('home')
#         else:
#             return render(request, 'registration/login.html', {'form': form})
#     else:
#         form = LoginForm()
#         return render(request, 'registration/login.html', {'form': form})
        # form = form_.UserCreationForm(request.POST)
        # # form_.
        # if form.is_valid():
        #     login(request, form)

    #              # authenticate(request , email=request.POST['email'],password=request.POST['password'])
    #     # myform = form_.CustomAuthenticationForm
    #     # form = AuthenticationForm(request.POST)
    #     username = request.POST['email']
    #     password = request.POST['password']
    #     user =authenticate(request, username=username,password=password)
    #     if user :
    #         login(request,user, backend=AUTHENTICATION_BACKENDS)

    # # form.username()
    # # user = authenticate(request, username=form.username(), password=form.password())
    #     if user != None:
    #         return redirect('home')
    #     else:
    #     #     form = form_.CustomAuthenticationForm()
    #         print('hi')
    #     return render(request, 'registration/login.html',{'form': form_.AuthenticationForm})
    #
    # return render(request, 'registration/login.html', {'form': form_.AuthenticationForm})
