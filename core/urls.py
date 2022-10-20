from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
#import render
from django.shortcuts import render
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

]
