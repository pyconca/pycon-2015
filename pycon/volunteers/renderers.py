from django_medusa.renderers import StaticSiteRenderer

class VolunteersRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/en/volunteers/",
            "/fr/volunteers/"
        ])

renderers = [VolunteersRenderer,]
