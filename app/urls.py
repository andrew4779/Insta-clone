from unicodedata import name
from  django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name= 'profile'),
    
]