from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here

