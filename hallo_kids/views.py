from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello Kids!!!")

def about(request):
    return HttpResponse("This is the about page")
