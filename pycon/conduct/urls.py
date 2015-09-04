from django.conf.urls import url
from pycon.conduct.views import ConductView

urlpatterns = [
    url(r"^$", ConductView.as_view(), name='conduct'),
]
