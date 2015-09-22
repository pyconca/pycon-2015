# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_presentation_proposal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='proposal_id',
            field=models.PositiveIntegerField(verbose_name='Proposal ID', unique=True),
        ),
    ]
