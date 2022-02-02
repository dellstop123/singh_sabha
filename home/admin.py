from django.contrib import admin

# Register your models here.
from .models import Contact, Donation, News

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','date')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('description','document','link','uploaded_at')    

admin.site.register(Contact)
admin.site.register(Donation,DonationAdmin)
admin.site.register(News, NewsAdmin)