from django.contrib import admin
from pycon.sponsors.models import Sponsor, Type


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    exclude = ('level',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'order')


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Type, TypeAdmin)
