# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0005_auto_20150923_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.CharField(max_length=64),
        ),
    ]
