from django.contrib import admin

# Register your models here.
from .models import Contact, Donation, News, Programme, About, Gallery, Carousel


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','subject','message')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','date')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('description','document','link','uploaded_at')   

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('description','image','uploaded_at')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('name','title','image')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image','title')

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image','title')                 

admin.site.register(Contact,ContactAdmin)
admin.site.register(Donation,DonationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Carousel,CarouselAdmin)