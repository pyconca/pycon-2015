from pycon.core.views import PyconTemplateView


class VenueView(PyconTemplateView):
    template_name = 'venue/venue.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'location': "123 Benton Road",
        })
