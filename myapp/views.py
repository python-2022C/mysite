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
        'list': [1,2,3,4,5,6,7,8,9,10],
        'products': {
            'product1': 'Laptop',
            'product2': 'Desktop',
        }

    }
  
    return render(request, 'home.html',context=context)