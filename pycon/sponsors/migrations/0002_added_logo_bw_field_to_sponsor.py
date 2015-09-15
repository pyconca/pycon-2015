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
            field=models.CharField(max_length=64, choices=[('1', 'Diamond'), ('2', 'Gold'), ('3', 'Silver'), ('4', 'Bronze'), ('5', 'Lanyard'), ('6', 'Workshop'), ('7', 'Party'), ('8', 'Travel'), ('9', 'Sprint'), ('10', 'Hosting'), ('11', 'Diversity'), ('12', 'Community')]),
        ),
    ]
