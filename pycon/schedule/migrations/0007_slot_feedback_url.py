# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_remove_presentation_feedback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='feedback_url',
            field=models.URLField(blank=True),
        ),
    ]
