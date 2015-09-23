# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, migrations
from django.utils import translation
from pycon.sponsors.enums import SponsorLevels


def from_level_to_type(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Sponsor = apps.get_model("sponsors", "Sponsor")
    Type = apps.get_model("sponsors", "Type")
    levels = dict(SponsorLevels.choices)
    translation.activate('fr')
    for sponsor in Sponsor.objects.all():
        num = int(sponsor.level) * 100
        en = levels[sponsor.level]
        fr = translation.ugettext(levels[sponsor.level])

        try:
            type = Type.objects.get(
                order=num,
                name_en=en,
                name_fr=fr,
            )
        except ObjectDoesNotExist:
            type = Type.objects.create(
                order=num,
                name_en=en,
                name_fr=fr,
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
