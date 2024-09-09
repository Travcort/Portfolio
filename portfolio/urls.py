from django.contrib import admin
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls, name='mainAdmin'),
    path('', views.home, name='home')
]