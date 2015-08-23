from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin

from pycon.home.views import HomeView

urlpatterns = [
    url(r"^$", HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]

if getattr(settings, 'DEBUG'):
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
