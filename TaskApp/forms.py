from django.forms import ModelForm, Form
from .models import *

#-------------- user creation / registration imports -----------------#

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#-------------- user login imports -----------------#

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2',]