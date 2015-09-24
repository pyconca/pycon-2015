from pycon.core.views import PyconTemplateView
from pycon.sponsors.models import Sponsor


class SponsorView(PyconTemplateView):
    template_name = 'sponsors/sponsor.html'

    def get(self, request):
        sponsors_list = []
        sponsors = Sponsor.objects.filter(type__isnull=False).order_by('type__order').select_related('type')
        for sponsor in sponsors:
            for sponsor_list in sponsors_list:
                if sponsor.type.id == sponsor_list[0].id:
                    sponsor_list.append(sponsor)
            else:
                sponsors_list.append([sponsor])
        return self.render_to_response({
            'sponsor_levels': sponsors_list,
        })
