from django.contrib import admin

# Register your models here.
from .models import Contact, Donation, News, Programme


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','subject','message')

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','date')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('description','document','link','uploaded_at')   

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('description','image','uploaded_at')      

admin.site.register(Contact,ContactAdmin)
admin.site.register(Donation,DonationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Programme, ProgrammeAdmin)