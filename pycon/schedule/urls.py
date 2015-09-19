from django.conf.urls import url
from pycon.schedule.views import ScheduleView, TalkDetailView

urlpatterns = [
    url(r"^(?P<pk>[0-9]+)/$", TalkDetailView.as_view(), name='schedule_talk_detail'),
    url(r"^$", ScheduleView.as_view(), name='schedule'),
]
