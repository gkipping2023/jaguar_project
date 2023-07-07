from django.shortcuts import render
from store.models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()[0:6]
    return render(request,'jaguar/home.html',{'product': product})

def about (request):
    return render(request, 'jaguar/about.html')