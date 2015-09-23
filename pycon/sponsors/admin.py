from django.contrib import admin
from pycon.sponsors.models import Sponsor, Type


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')


class TypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Type, TypeAdmin)
