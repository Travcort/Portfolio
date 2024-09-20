from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'facts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.jokes, name='main')
]