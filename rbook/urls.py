from . import views
from django.urls import path

urlpatterns = [
    path('', views.tmp_view, name = 'home'),
]