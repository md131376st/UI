from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Request
from django.contrib.auth.forms import AuthenticationForm

# class SignUpForm(UserCreationForm):
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_Birth', 'contact', 'user_name', 'national_number','password']
        # fields = ('ایمیل', 'نام', 'نام خانوادگی', 'تاریخ تولد','شماره ملی')


class Home(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'user_name', 'contact', 'national_number', 'date_Birth',
     'avatar']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['writer', 'subject', 'text']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="آدرس ایمیل",max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
    password = forms.CharField(label="رمز عبور", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
    # class Meta:
    #     model = User
    #     fields = ['email', 'password']

# class CustomAuthenticationForm(AuthenticationForm):

    # pass
#