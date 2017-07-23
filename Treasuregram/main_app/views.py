from django.shortcuts import render
from django.Http import HttpResponse

def index(Request):
    return HttpResponse('<h1> Hello world !</h1>')

# Create your views here.
