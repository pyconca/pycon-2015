from django.conf.urls import url

from pycon.sponsors.views import SponsorView

urlpatterns = [
    url(r"^$", SponsorView.as_view(), name='sponsor'),
]
