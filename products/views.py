from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index


def index_view(request):
    return render(request, 'index.html')


def product_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def new(request):
    return HttpResponse('New Products')
