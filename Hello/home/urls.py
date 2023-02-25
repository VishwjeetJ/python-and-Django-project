from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
   path("", views.index, name='name'),   
   path("about", views.about, name='about'),   
   path("category", views.category, name='category'), 
   path("contact", views.contact, name='contact'),   
 ]
