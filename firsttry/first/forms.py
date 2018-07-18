from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# class SignUpForm(UserCreationForm):
class SignUpForm(forms.ModelForm):
    # email = forms.EmailField(unique=True, help_text="1@gmail.com")
    # first_name = forms.CharField( max_length=30, blank=True)
    # last_name = forms.CharField( max_length=30, blank=True)
    # date_Birth = forms.DateTimeField( blank=True, help_text="روز-ماه-سال")
    # contact = forms.CharField(max_length=30, blank=True)
    # user_gender = forms.CharField( choices=((0, 'زن'), (1, 'مرد')), max_length=30, default='زن')
    # user_name = forms.CharField( unique=True, max_length=30)
    # forms.

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_Birth', 'contact', 'user_name', 'national_number','password']
        # fields = ('ایمیل', 'نام', 'نام خانوادگی', 'تاریخ تولد','شماره ملی')


class Home(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'user_name', 'contact', 'national_number', 'date_Birth',
                  'avatar']

