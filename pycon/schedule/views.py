from django.shortcuts import get_object_or_404

from pycon.core.views import PyconTemplateView

from pycon.schedule.models import Day
from pycon.schedule.timetable import TimeTable

class ScheduleView(PyconTemplateView):
    template_name = 'schedule/schedule.html'
    
    def get(self, request):
        days_qs = Day.objects.all()
        days = [TimeTable(day) for day in days_qs]
        
        return self.render_to_response({
            'days': days
        })


class TalkDetailView(PyconTemplateView):
    template_name = 'schedule/talk_detail.html'
    
    def get(self, request, *args, **kwargs):
        talk = get_object_or_404(Talk, pk=kwargs['pk'])
        
        return self.render_to_response({'talk': talk})
