from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'partial/body.html') 

def about(request):
    return render(request,'partial/about.html')

def location(request):
    return render(request,'partial/location.html') 

def contact(request):
    return render(request,'partial/contact.html')       