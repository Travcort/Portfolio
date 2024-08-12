"""
URL configuration for jokes app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'jokes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('programming/', views.programming, name="programming"),
    path('pun/', views.pun, name="pun"),
    path('dark/', views.dark, name="dark"),
    path('miscellaneous/', views.miscellaneous, name="miscellaneous"),
    path('spooky/', views.spooky, name="spooky"),
    path('mystery/', views.mystery, name="mystery")
]