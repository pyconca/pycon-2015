from django.utils.translation import ugettext_lazy as _


class SponsorLevels():
    DIAMOND = 'diamond'
    GOLD = 'gold'
    SILVER = 'silver'
    BRONZE = 'bronze'

    choices = (
        (DIAMOND, _('Diamond')),
        (GOLD, _('Gold')),
        (SILVER, _('Silver')),
        (BRONZE, _('Bronze')),
    )
