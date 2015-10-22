from django.utils.translation import activate

from django_medusa.renderers import StaticSiteRenderer

from .models import Presentation

class ScheduleRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set([
            "/en/schedule/",
            "/fr/schedule/"
        ])
        
        presentation_list = Presentation.objects.all()
        
        for p in presentation_list:
            activate('en')
            paths.add(p.get_absolute_url())
            activate('fr')
            paths.add(p.get_absolute_url())
        
        return list(paths)

renderers = [ScheduleRenderer,]
