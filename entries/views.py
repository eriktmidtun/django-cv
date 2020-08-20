from django.shortcuts import render

from .models import Section, Sidebar


def home(request):
    Sections = Section.objects.exclude(visible=False)
    Sidebars = Sidebar.objects.exclude(visible=False)
    for sec in Sections.all():
        print("Section", sec, sec.order_priority)
        for entry in sec.entries.all():
            print("entry", entry, entry.order_priority)
            

    return render(request, 'entries/content.html', {'Sections': Sections, 'Sidebars' : Sidebars})