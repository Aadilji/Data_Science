from django.contrib import admin
from django.urls import path 
from hello_app import views

urlpatterns = [
    path('',views.index, name='hello_app'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services')

]
