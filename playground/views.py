from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()
    
    for product in query_set: # query_set is a list of objects of type Product
        print(product) # print the object itself (not the name)
    return render(request, 'hello.html', {'name': 'Mosh'})
