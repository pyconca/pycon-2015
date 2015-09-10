from django.utils.translation import ugettext_lazy as _


class SponsorLevels():
    DIAMOND = 'diamond'
    GOLD = 'gold'
    SILVER = 'silver'
    BRONZE = 'bronze'
    LANYARD = 'lanyard'
    WORKSHOP = 'workshop'
    PARTY = 'party'
    TRAVEL = 'travel'
    SPRINT = 'sprint'
    HOSTING = 'hosting'
    DIVERSITY = 'diversity'
    COMMUNITY = 'community'

    choices = (
        (DIAMOND, _('Diamond')),
        (GOLD, _('Gold')),
        (SILVER, _('Silver')),
        (BRONZE, _('Bronze')),
        (LANYARD, _('Lanyard')),
        (WORKSHOP, _('Workshop')),
        (PARTY, _('Party')),
        (TRAVEL, _('Travel')),
        (SPRINT, _('Sprint')),
        (HOSTING, _('Hosting')),
        (DIVERSITY, _('Diversity')),
        (COMMUNITY, _('Community')),
    )
