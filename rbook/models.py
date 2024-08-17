from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique = True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name = "posts")
    content = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


