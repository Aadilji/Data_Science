from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, This is Aadil")

def about(request):
    text = '<h1>This is about</h1>'
    return HttpResponse(text)

def services(request):
    return HttpResponse("Contact Services") 

