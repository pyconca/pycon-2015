from collections import defaultdict
from pycon.core.views import PyconTemplateView
from pycon.sponsors.models import Sponsor


class SponsorView(PyconTemplateView):
    template_name = 'sponsors/sponsor.html'

    def get(self, request):
        sponsors = defaultdict(list)
        for sponsor in Sponsor.objects.all():
            sponsors[sponsor.level].append(sponsor)
        return self.render_to_response({
            'sponsors': sponsors,
        })
