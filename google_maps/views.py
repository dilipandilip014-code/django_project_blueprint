from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world. you're at the google_maps app index.")