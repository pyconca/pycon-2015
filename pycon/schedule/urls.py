from django.conf.urls import url
from pycon.schedule.views import ScheduleView, PresentationView

urlpatterns = [
    url(
        regex = r"^$",
        view = ScheduleView.as_view(),
        name = 'schedule'
    ),
    url(
        regex = r"^(?P<pk>[0-9]+)/$",
        view = PresentationView.as_view(),
        name = 'schedule_presentation_detail'
    ),
]
