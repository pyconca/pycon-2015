import os
from django.db import models

from pycon.sponsors.enums import SponsorLevels


class Sponsor(models.Model):

    def upload_path(self, filename):
        return os.path.basename(filename)

    description_en = models.TextField(max_length=2048)
    description_fr = models.TextField(max_length=2048)
    logo = models.ImageField(max_length=512, upload_to=upload_path)
    logo_bw = models.ImageField(max_length=512, upload_to=upload_path)
    name = models.CharField(max_length=128)
    level = models.CharField(max_length=64, choices=SponsorLevels.choices)
    twitter_en = models.CharField(max_length=32, blank=True)
    twitter_fr = models.CharField(max_length=32, blank=True)
    url_website_en = models.URLField(blank=True)
    url_website_fr = models.URLField(blank=True)

