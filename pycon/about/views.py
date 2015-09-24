from pycon.about.models import Volunteer
from pycon.core.views import PyconTemplateView

from pycon.sponsors.models import Sponsor


class AboutView(PyconTemplateView):
    template_name = 'about/about.html'

    def get(self, request):
        return self.render_to_response({
            'sponsors': Sponsor.objects.filter(type__isnull=False).order_by('-type__order'),
            'volunteers': Volunteer.objects.all().order_by('name'),
        })
