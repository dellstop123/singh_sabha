from django.urls import path
from .views import (index,about,location, contact,donors,programme)


urlpatterns = [
    path(r'',index,name='index'),
    path(r'about',about,name='about'),
    path('location',location,name='location'),
    path('contact',contact,name='contact'),
    path('donors',donors,name='donors'),
    path('programme',programme,name='programme'),

]