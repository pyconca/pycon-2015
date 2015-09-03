from django.contrib import admin
from pycon.about.models import Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(Volunteer, VolunteerAdmin)
