from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib import messages
import json
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from funding.models import Categoria

def home(request):
   
   return render(request,'index.html')

def do_categorias(request):
    categoria=Categoria.objects.all()
    return render(request,'campanias.html',{'categorias':categoria})