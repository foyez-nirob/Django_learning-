# views where every logic are written 
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')