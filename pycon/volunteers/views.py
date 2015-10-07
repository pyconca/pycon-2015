from pycon.about.models import Volunteer
from pycon.core.views import PyconTemplateView

from pycon.volunteers.models import Volunteer


class VolunteersView(PyconTemplateView):
    template_name = 'volunteers/volunteers.html'

    def get(self, request):
        return self.render_to_response({
            'volunteer_list': Volunteer.objects.all()})
