from pycon.core.views import PyconTemplateView

from pycon.sponsors.models import Sponsor


class HomeView(PyconTemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        return self.render_to_response({
            'sponsors': Sponsor.objects.all().order_by('level'),
        })
