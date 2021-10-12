from ProyectoWeb.apps import ProyectowebConfig
from email import message
from typing import ValuesView
from django import forms
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm



def home(request):

    return render(request, "ProyectoWeb/home.html")

def tienda(request):

    return render(request, "ProyectoWeb/tienda.html")

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Creado') 
            return redirect('registrar')
    else :
        form = UserRegisterForm()
        
    context ={ 'form': form}
    return render(request,"ProyectoWeb/registrar.html", context )   
    
    
    #return render(request, "ProyectoWeb/admin.html")