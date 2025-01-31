from django.urls import path
from .views import data, loop, index, about, contact, reports

urlpatterns = [
    path('data/', data, name='data'),
    path('loop/', loop, name='loop'),
    path('', index, name='index'),  
    path('about/', about, name='about'),  
    path('contact/', contact, name='contact'),  
    path('reports/', reports, name='reports'), 
]
