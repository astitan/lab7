from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'main/laba7.html')