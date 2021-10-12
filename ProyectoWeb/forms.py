from typing import Tuple
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import EmailField


class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField(label='Corre electronico', widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
        help_texts = {k: "" for k in fields}
        
    