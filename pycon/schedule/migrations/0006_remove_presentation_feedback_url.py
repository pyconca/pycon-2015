# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_presentation_feedback_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='feedback_url',
        ),
    ]
