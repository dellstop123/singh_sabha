from django.shortcuts import render
from .form import ContactForm
from django.contrib import messages
from .models import Donation, News, Programme, About, Gallery, Carousel
from translate import Translator
# Create your views here.
import pyttsx3
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 125)
speaker.setProperty('voice', "com.apple.speech.synthesis.voice.lekha")
 

def trans(request,text):
    say_lang="en"
    convert_lang="hi-IN"
    translator=Translator(from_lang = say_lang,to_lang=convert_lang)
    sentence=text
    translation=translator.translate(text)
    # print(translation)
    return translation

def index(request):         
    donate = donation(request)
    events = news(request)
    galery = gallery(request)
    slider = carousel(request)
    context = {"donate":donate,"events":events,"gallery":galery,"carousel":slider}    
    return render(request,'partial/body.html',context) 

def about(request):
    about = About.objects.values()
    for voice in voices: 
        print("Voice:") 
        print(" - ID: %s" % voice.id) 
        print(" - Name: %s" % voice.name) 
        print(" - Languages: %s" % voice.languages) 
        print(" - Gender: %s" % voice.gender) 
        print(" - Age: %s" % voice.age)
    txt =  trans(request,'E han Sardar Gurcharan Singh')
    print(txt)
    speaker.say(txt)
    speaker.runAndWait()
    # speaker.stop()
    img = []
    title = []
    name =[]
    for i in range(about.count()):
        img.append(about[i]['image'])
        title.append(about[i]['title'])
        name.append(about[i]['name'])
    abt = zip(img,title,name)
    slider = carousel(request)
    
    context = {"about":abt,"carousel":slider}
    return render(request,'partial/about.html',context)

def programme(request):
    programme = Programme.objects.values().order_by('-uploaded_at')
    desc =[]
    img = []
    date =[]
    for i in range(programme.count()):
            desc.append(programme[i]['description']),
            img.append(programme[i]['image']),
            date.append(programme[i]['uploaded_at'])
          
    program = zip(desc,img,date)
    slider = carousel(request)
    context = {"programme":program,"carousel":slider}
    return render(request,'partial/programme.html',context)    

def donors(request):
    donate = donation(request)
    slider = carousel(request)
    context = {"donate":donate,"carousel":slider} 
    return render(request,'partial/donors.html',context)    

def location(request):
    slider = carousel(request)
    context = {"carousel":slider}
    return render(request,'partial/location.html',context) 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully')
            # return render(request, 'partial/contact.html')
    form = ContactForm()
    slider = carousel(request)
    context = {'form': form,"carousel":slider}
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


def gallery(request):
    gallery = Gallery.objects.values()
    image =[]
    for i in range(gallery.count()):
        image.append(gallery[i]['image'])
    gall = image
    return gall

def carousel(request):
    carousel = Carousel.objects.values()
    image =[]
    for i in range(carousel.count()):
        image.append(carousel[i]['image'])
    car = image
    return car