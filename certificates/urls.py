from django.urls import path
from . import views

urlpatterns =[
    path('addcertificats/', views.addcertificates, name='addcertificates'),
    path('set_certificates/', views.set_certificates, name='certificates'),
    path('search_certificates/', views.search_certificates, name='search_certificates'),
    
]