from django.conf.urls import include, url
from django.contrib import admin

from pycon.home.views import HomeView

urlpatterns = [
    url(r"^$", HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
