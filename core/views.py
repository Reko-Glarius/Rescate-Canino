from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def adoption(request):
    return render(request, "core/adoption.html")

def contact(request):
    return render(request, "core/contact.html")