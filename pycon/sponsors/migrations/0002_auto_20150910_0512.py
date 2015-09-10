# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.CharField(choices=[('diamond', 'Diamond'), ('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze'), ('lanyard', 'Lanyard'), ('workshop', 'Workshop'), ('party', 'Party'), ('travel', 'Travel'), ('sprint', 'Sprint'), ('hosting', 'Hosting'), ('diversity', 'Diversity'), ('community', 'Community')], max_length=64),
        ),
    ]
