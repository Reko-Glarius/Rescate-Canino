from django.shortcuts import render
from .models import Dog

# Create your views here.
def adoption(request):
    dogs=Dog.objects.all()
    return render(request, "dogs/adoption.html", {"dogs": dogs})