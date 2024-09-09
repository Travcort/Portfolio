from django.contrib import admin
from django.urls import path
from . import views

app_name = 'potter'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('spells/', views.spells, name='spells'),
    path('characters/', views.characters, name='characters'),
    path('houses/', views.houses, name='houses'),
    path('books/', views.books, name='books')
]

