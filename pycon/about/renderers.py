from django_medusa.renderers import StaticSiteRenderer

class AboutRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/en/about/",
            "/fr/about/"
        ])

renderers = [AboutRenderer,]
