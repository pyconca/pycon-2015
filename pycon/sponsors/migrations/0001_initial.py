# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pycon.sponsors.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description_en', models.TextField(max_length=2048)),
                ('description_fr', models.TextField(max_length=2048)),
                ('logo', models.ImageField(upload_to=pycon.sponsors.models.Sponsor.upload_path, max_length=512)),
                ('name', models.CharField(max_length=128)),
                ('level', models.CharField(choices=[('diamond', 'Diamond'), ('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], max_length=64)),
                ('twitter_en', models.CharField(blank=True, max_length=32)),
                ('twitter_fr', models.CharField(blank=True, max_length=32)),
                ('url_website_en', models.URLField(blank=True)),
                ('url_website_fr', models.URLField(blank=True)),
            ],
        ),
    ]
