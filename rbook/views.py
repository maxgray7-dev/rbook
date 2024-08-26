from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def my_rbook(request):
    return HttpResponse ('Welcome to my Recipe Book!!')

def tmp_view(request):
  template = loader.get_template('rbook/index.html')
  return HttpResponse(template.render())