from django.utils.translation import ugettext_lazy as _


class SponsorLevels():
    DIAMOND = '1'
    GOLD = '2'
    SILVER = '3'
    BRONZE = '4'
    LANYARD = '5'
    WORKSHOP = '6'
    PARTY = '7'
    TRAVEL = '8'
    SPRINT = '9'
    HOSTING = '10'
    DIVERSITY = '11'
    COMMUNITY = '12'

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

    reverse = {
        DIAMOND: 'diamond',
        GOLD: 'gold',
        SILVER: 'silver',
        BRONZE: 'bronze',
        LANYARD: 'lanyard',
        WORKSHOP: 'workshop',
        PARTY: 'party',
        TRAVEL: 'travel',
        SPRINT: 'sprint',
        HOSTING: 'hosting',
        DIVERSITY: 'diversity',
        COMMUNITY: 'community',
    }