from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'partial/body.html') 

def about(request):
    return render(request,'partial/about.html')