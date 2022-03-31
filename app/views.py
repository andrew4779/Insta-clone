from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here

@login_required(login_url='/accounts/login/')
def index(request):
    # get all the images from the database and order them by the date they were created
    images = Image.objects.all().order_by('-image_date')
    return render(request, 'index.html', {'images': images})
