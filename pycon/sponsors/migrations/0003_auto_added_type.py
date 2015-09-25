# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_added_logo_bw_field_to_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name_en', models.CharField(max_length=255)),
                ('name_fr', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='type',
            field=models.ForeignKey(null=True, to='sponsors.Type'),
        ),
    ]
