import os
from django.db import models

from pycon.sponsors.enums import SponsorLevels


class Sponsor(models.Model):

    def upload_path(self, filename):
        return os.path.basename(filename)

    name_en = models.CharField(max_length=128)
    name_fr = models.CharField(max_length=128)
    description_en = models.TextField(max_length=512)
    description_fr = models.TextField(max_length=512)
    logo = models.ImageField(max_length=512, upload_to=upload_path)
    level = models.CharField(max_length=64, choices=SponsorLevels.choices)
    url_twitter = models.URLField(blank=True)
    url_website = models.URLField(blank=True)

