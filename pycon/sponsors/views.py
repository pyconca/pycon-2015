from pycon.core.views import PyconTemplateView
from pycon.sponsors.models import Sponsor


class SponsorView(PyconTemplateView):
    template_name = 'sponsor.html'

    def get(self, request):
        return self.render_to_response({
            'sponsors': Sponsor.objects.all().order_by('level'),
        })
