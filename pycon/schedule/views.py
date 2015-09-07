from pycon.core.views import PyconTemplateView


class ScheduleView(PyconTemplateView):
    template_name = 'schedule/schedule.html'

    def get(self, request):
        return self.render_to_response({})
