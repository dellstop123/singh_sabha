from django.shortcuts import render
from .form import ContactForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'partial/body.html') 

def about(request):
    return render(request,'partial/about.html')

def location(request):
    return render(request,'partial/location.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully')
            # return render(request, 'partial/contact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request,'partial/contact.html',context)