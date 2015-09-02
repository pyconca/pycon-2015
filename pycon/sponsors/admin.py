from django.contrib import admin
from pycon.sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'level')


admin.site.register(Sponsor, SponsorAdmin)
