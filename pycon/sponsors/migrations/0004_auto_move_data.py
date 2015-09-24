# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, migrations
from django.utils import translation


def from_level_to_type(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    levels_en = {
        '1': 'Diamond',
        '2': 'Gold',
        '3': 'Silver',
        '4': 'Bronze',
        '5': 'Lanyard',
        '6': 'Workshop',
        '7': 'Party',
        '8': 'Travel',
        '9': 'Sprint',
        '10': 'Hosting',
        '11': 'Diversity',
        '12': 'Community',
    }
    levels_fr = {
        '1': 'Diamant',
        '2': 'Or',
        '3': 'Argent',
        '4': 'Bronze',
        '5': 'Lanyard',
        '6': 'Atelier',
        '7': 'Party',
        '8': 'Déplacement',
        '9': 'Sprint',
        '10': 'Hébergement Web',
        '11': 'Diversité',
        '12': 'Communauté',
    }

    Sponsor = apps.get_model("sponsors", "Sponsor")
    Type = apps.get_model("sponsors", "Type")
    translation.activate('fr')
    for sponsor in Sponsor.objects.all():
        try:
            type = Type.objects.get(
                order=int(sponsor.level) * 100,
                name_en=levels_en[sponsor.level],
                name_fr=levels_fr[sponsor.level],
            )
        except ObjectDoesNotExist:
            type = Type.objects.create(
                order=int(sponsor.level) * 100,
                name_en=levels_en[sponsor.level],
                name_fr=levels_fr[sponsor.level],
            )
        sponsor.type = type
        sponsor.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sponsors', '0003_auto_added_type'),
    ]

    operations = [
        migrations.RunPython(from_level_to_type),
    ]
