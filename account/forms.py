from django import forms
from .models import *
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
class LoginForm(forms.Form):
 
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput)