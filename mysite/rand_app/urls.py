from django.contrib import admin
from django.urls import path,include
from rand_app import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('', views.display),
    
]
