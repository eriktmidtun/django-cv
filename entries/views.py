from django.shortcuts import render

from .models import Section

def home(request):
    Sections = Section.objects
    return render(request, 'entries/home.html', {'Sections': Sections})