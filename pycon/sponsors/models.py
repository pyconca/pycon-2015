import os
from django.db import models


class Sponsor(models.Model):

    def upload_path(self, filename):
        return os.path.basename(filename)

    description_en = models.TextField(max_length=2048)
    description_fr = models.TextField(max_length=2048)
    logo = models.ImageField(max_length=512, upload_to=upload_path)
    logo_bw = models.ImageField(max_length=512, upload_to=upload_path)
    name = models.CharField(max_length=128)
    type = models.ForeignKey('Type')
    level = models.CharField(max_length=64)
    twitter_en = models.CharField(max_length=32, blank=True)
    twitter_fr = models.CharField(max_length=32, blank=True)
    url_website_en = models.URLField(blank=True)
    url_website_fr = models.URLField(blank=True)


class Type(models.Model):

    name_en = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)
    order = models.IntegerField()
