from django.utils.translation import ugettext_lazy as _


class SponsorLevels():
    DIAMOND = '1'
    GOLD = '2'
    SILVER = '3'
    BRONZE = '4'

    choices = (
        (DIAMOND, _('Diamond')),
        (GOLD, _('Gold')),
        (SILVER, _('Silver')),
        (BRONZE, _('Bronze')),
    )
