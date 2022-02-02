from django.shortcuts import render
from .form import ContactForm
from django.contrib import messages
from .models import Donation, News
# Create your views here.

def index(request):
    # donation(request)
    # donation = Donation.objects.values().order_by('-date')[:5]
    # name =[]
    # price = []
    # date =[]
    # for i in range(donation.count()):
    #         name.append(donation[i]['name']),
    #         price.append(donation[i]['price']),
    #         date.append(donation[i]['date'])
          
    donate = donation(request)
    events = news(request)
    context = {"donate":donate,"events":events}    
    return render(request,'partial/body.html',context) 

def about(request):
    return render(request,'partial/about.html')

def donors(request):
    donate = donation(request)
    context = {"donate":donate} 
    return render(request,'partial/donors.html',context)    

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


def donation(request):
    donation = Donation.objects.values().order_by('-date')[:5]
    name =[]
    price = []
    date =[]
    for i in range(donation.count()):
            name.append(donation[i]['name']),
            price.append(donation[i]['price']),
            date.append(donation[i]['date'])
          
    donate = zip(name,price,date)    
    return donate

def news(request):
    news = News.objects.values().order_by('-uploaded_at')
    desc =[]
    docs =[]
    link =[]
    for i in range(news.count()):
        desc.append(news[i]['description']),
        docs.append(news[i]['document']),
        link.append(news[i]['link'])

    events = zip(desc,docs,link)
    return events    