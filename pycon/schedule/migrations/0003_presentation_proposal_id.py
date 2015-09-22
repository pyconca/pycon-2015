# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_slot_content_override'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='proposal_id',
            field=models.PositiveIntegerField(default=82),
            preserve_default=False,
        ),
    ]
