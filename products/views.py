from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "products/prod.html")

def new(request):
    return render(request, "products/new_product.html")