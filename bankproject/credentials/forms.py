# from .models import UserProfile
# from django import forms
#
#
# class Step1Form(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#
# class Step2Form(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'dob', 'address']
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']