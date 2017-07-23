from django.shortcuts import render
from django.Http import HttpResponse

def index(Request):
    return HttpResponse('<h> Hello world !</h>')

# Create your views here.
