from django.shortcuts import render

from .models import Section, Sidebar


def home(request):
    Sections = Section.objects.exclude(visible=False)
    Sidebars = Sidebar.objects.exclude(visible=False)

    return render(request, 'entries/content.html', {'Sections': Sections, 'Sidebars' : Sidebars})