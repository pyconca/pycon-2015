import csv

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from pycon.mailing.models import Mailing


def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.

    https://djangosnippets.org/snippets/1697/
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format('mailing_list')
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    writer.writerow(field_names)
    for obj in Mailing.objects.all():
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


export_as_csv.short_description = "Export all objects as csv file"


class MailingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    actions = [export_as_csv]


admin.site.register(Mailing, MailingAdmin)
