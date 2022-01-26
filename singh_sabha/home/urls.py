from django.urls import path
from .views import (index,about)


urlpatterns = [
    path(r'index',index,name='index'),
    path(r'about',about,name='about'),
    # path('',index,name='index'),
]