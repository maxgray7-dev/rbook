from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_rbook(request):
    return HttpResponse ('Welcome to my Recipe Book!')
