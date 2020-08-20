from django.contrib import admin

from .models import Section, Entry, Sentry, Sidebar, SiteConfig
from solo.admin import SingletonModelAdmin


admin.site.register(SiteConfig, SingletonModelAdmin)
admin.site.register(Section)
admin.site.register(Entry)
admin.site.register(Sentry)
admin.site.register(Sidebar)


config = SiteConfig.objects.get()

# get_solo will create the item if it does not already exist
config = SiteConfig.get_solo()