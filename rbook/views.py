from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Post

# Create your views here.
def my_rbook(request):
    return HttpResponse ('Welcome to my Recipe Book!!')

def tmp_view(request):
  template = loader.get_template('rbook/index.html')
  return HttpResponse(template.render())

class PostList(generic.ListView):
  queryset = Post.objects.all()
  template_name = "rbook/index.html"
  paginate_by = 6

def recipe_detail(request, slug):
  queryset=Post.objects.all()
  post=get_object_or_404(queryset,slug=slug)

  return render(
        request,
        "rbook/recipe_detail.html",
        {"post": post,
        "author": "Maksim Popov",
        }
  )
        