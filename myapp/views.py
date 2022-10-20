from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'username': 'John',
        'age': 25,
        'email': 'john@gmail.com',
        'address': '123 Main St',
        'phone': '555-555-5555'
    }
  
    return render(request, 'home.html',context=context)