from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique = True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name = "posts")
    content = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["created_on"]


