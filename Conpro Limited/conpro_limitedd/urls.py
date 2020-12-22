"""Defines URL patterns for conpro_limitedd."""

from django.urls import path

from .import views

app_name = 'conpro_limitedd'

urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    #About page
    path('about/', views.about, name= 'about'),
    #Services page
    path('services/', views.services, name= 'services'),
    #Projects page
    path('projects/', views.projects, name='projects'),
    #Contacts page
    path('contact/', views.contact, name= 'contact')
]