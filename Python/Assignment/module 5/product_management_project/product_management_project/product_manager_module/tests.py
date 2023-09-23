from django.test import TestCase
from django.shortcuts import render
from .models import Product

# Create your tests here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_manager/product_list.html', {'products': products})


