from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Tout baigne !')

# Create your views here.
