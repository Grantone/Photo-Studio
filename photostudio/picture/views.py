from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.


def index(request):
    images = Image.get_images()

    return render(request, 'all-images/index.html', {"images": images})
