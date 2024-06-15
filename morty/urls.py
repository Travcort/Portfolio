from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'morty'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="morty-landing"),
    path('characters/', views.characterMain, name="characters"),
    path('locations/', views.locationMain, name="locations")
]