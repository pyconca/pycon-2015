from django_medusa.renderers import StaticSiteRenderer

class ConductRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/en/conduct/",
            "/fr/conduct/"
        ])

renderers = [ConductRenderer,]
