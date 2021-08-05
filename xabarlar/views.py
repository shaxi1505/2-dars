from django.shortcuts import render
from django.views.generic import ListView
from .models import Maqola
# Create your views here.
class Asosiysahifa(ListView):
    template_name = 'asosiy.html'
    model = Maqola
