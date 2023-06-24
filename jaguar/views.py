from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'jaguar/home.html')

def categories(request):
    return render(request, 'jaguar/categories.html')