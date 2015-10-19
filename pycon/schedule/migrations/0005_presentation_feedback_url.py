# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20150922_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='feedback_url',
            field=models.URLField(blank=True),
        ),
    ]
