from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Conpro Limited"""
    return render(request, 'conpro_limitedd/index.html')

def about(request):
    """The about page for Conpro Limited"""
    return render(request, 'conpro_limitedd/about.html')

def services(request):
    """The Service page for Conpro Limited"""
    return render(request, 'conpro_limitedd/services.html')

def projects(request):
    """The projects page for Conpro Limited"""
    return render(request, 'conpro_limitedd/projects.html')

def contact(request):
    """The contact page for Conpro Limited"""
    return render(request, 'conpro_limitedd/contact.html')