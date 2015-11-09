# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_slot_feedback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='youtube_hash',
            field=models.CharField(null=True, max_length=25, blank=True),
        ),
    ]
