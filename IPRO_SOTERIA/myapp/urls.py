from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('getReadings',views.getReadings, name='getReadings'),
    
]

