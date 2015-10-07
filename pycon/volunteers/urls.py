from django.conf.urls import url

from pycon.volunteers.views import AboutView

urlpatterns = [
    url(r"^$", VolunteersView.as_view(), name='volunteers'),
]
