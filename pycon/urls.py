from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from pycon.home.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r"^$", HomeView.as_view(), name='home'),
    url(r'^about/', include('pycon.about.urls')),
    url(r'^sponsors/', include('pycon.sponsors.urls')),
    url(r'^mailing/', include('pycon.mailing.urls')),
)

if getattr(settings, 'DEBUG'):
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
