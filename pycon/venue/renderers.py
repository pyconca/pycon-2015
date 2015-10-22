from django_medusa.renderers import StaticSiteRenderer

class VenueRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/en/venue/",
            "/fr/venue/"
        ])

renderers = [VenueRenderer,]
