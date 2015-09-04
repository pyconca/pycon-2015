from pycon.core.views import PyconTemplateView


class ConductView(PyconTemplateView):
    template_name = 'conduct/conduct.html'

    def get(self, request):
        return self.render_to_response({})
