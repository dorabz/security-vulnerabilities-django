from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import login
from django.core import serializers
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm



from .models import login
from random import randint
from xml.dom.pulldom import parseString, START_ELEMENT
from xml.sax.handler import feature_external_ges
from xml.sax import make_parser
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import subprocess
import pickle
import base64
import yaml
import json
from dataclasses import dataclass



def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login")

    else:
        form=UserCreationForm();
        return render(request,"registration/register.html",{"form":form,})

def home(request):
    if request.user.is_authenticated:
        return render(request,'vulnerable/home.html',)
    else:
        return redirect('login')

#Broken Access Control
def ba(request):
    if request.user.is_authenticated:
        return render(request,"attacks/BrokenAccess/ba.html")
    else:
        return redirect('login')
@csrf_exempt
def ba_lab(request):
    if request.user.is_authenticated:
        name = request.POST.get('name')
        password = request.POST.get('pass')
        if name:


            #if request.COOKIES.get('admin') == "1":
                #return render(request, 'attacks/BrokenAccess/ba_lab.html', {"data":"Hello admin! Here is you super secret message: We won't let Grinch take Christmas!"})
            if login.objects.filter(user='admin',password=password):
                html = render(request, 'attacks/BrokenAccess/ba_lab.html', {"data":"Hello admin! Here is you super secret message: We won't let Grinch take Christmas!"})
                #html.set_cookie("admin", "1",max_age=200);
                return html
            elif login.objects.filter(user=name,password=password):
                html = render(request, 'attacks/BrokenAccess/ba_lab.html',{"data":"Welcome Grinch!"} )
                #html.set_cookie("admin", "0",max_age=200);
                return html
            else:
                return render(request, 'attacks/BrokenAccess/ba_lab.html', {"data": "Oops: User not found"})

        else:
            return render(request,'attacks/BrokenAccess/ba_lab.html',{"data":"Please login with credentials"})
    else:
        return redirect('login')

#Sensitive Data Exposure


def data_exp(request):
    if request.user.is_authenticated:
        return  render(request,'attacks/DataExp/data_exp.html')
    else:
        return redirect('login')

def data_exp_lab(request):
    if request.user.is_authenticated:
        return  render(request,'attacks/DataExp/data_exp_lab.html')
    else:
        return redirect('login')
def robots(request):
    if request.user.is_authenticated:
        response = render(request,'attacks/DataExp/robots.txt')
        response['Content-Type'] =  'text/plain'
        return response

def error(request):
    return 

