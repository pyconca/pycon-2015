from django.conf.urls import url
from pycon.schedule.views import ScheduleView

urlpatterns = [
    url(r"^$", ScheduleView.as_view(), name='schedule'),
]
