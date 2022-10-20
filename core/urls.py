from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
#import render
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),

]
