from django_medusa.renderers import StaticSiteRenderer

class SponsorsRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/en/sponsors/",
            "/fr/sponsors/"
        ])

renderers = [SponsorsRenderer,]
