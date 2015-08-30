from django.conf.urls import url

from pycon.venue.views import VenueView

urlpatterns = [
    url(r"^$", VenueView.as_view(), name='venue'),
]
