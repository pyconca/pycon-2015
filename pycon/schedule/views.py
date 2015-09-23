from django.shortcuts import get_object_or_404

from pycon.core.views import PyconTemplateView

from pycon.schedule.models import Day, Presentation
from pycon.schedule.timetable import TimeTable

class ScheduleView(PyconTemplateView):
    template_name = 'schedule/schedule.html'
    
    def get(self, request):
        days_qs = Day.objects.all()
        days = [TimeTable(day) for day in days_qs]
        
        return self.render_to_response({
            'days': days
        })


class PresentationView(PyconTemplateView):
    template_name = 'schedule/presentation.html'
    
    def get(self, request, pk, *args, **kwargs):
        presentation = get_object_or_404(Presentation, pk=pk)
        
        return self.render_to_response({
            'p': presentation
        })
