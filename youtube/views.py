from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django is working!")

def home(request):
    return render(request,'youtube/home.html')