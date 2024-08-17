from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on',)
    search_fields = ['title', 'created_on']
    list_filter = ('author', 'title', 'created_on',)
    prepopulated_fields = {'slug': ('author',)}