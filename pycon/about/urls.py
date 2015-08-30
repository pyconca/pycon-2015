from django.conf.urls import url

from pycon.about.views import AboutView

urlpatterns = [
    url(r"^$", AboutView.as_view(), name='about'),
]
