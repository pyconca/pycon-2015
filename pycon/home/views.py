from django.views.generic.base import TemplateView

from pycon.sponsors.models import Sponsor


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return self.render_to_response({
            'sponsors': Sponsor.objects.all().order_by('level'),
        })
