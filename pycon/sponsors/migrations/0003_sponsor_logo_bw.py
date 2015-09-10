# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pycon.sponsors.models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20150910_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='logo_bw',
            field=models.ImageField(max_length=512, default='allo', upload_to=pycon.sponsors.models.Sponsor.upload_path),
            preserve_default=False,
        ),
    ]
