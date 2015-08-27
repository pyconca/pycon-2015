import os
from django.db import models

from pycon.sponsors.enums import SponsorLevels


class Sponsor(models.Model):

    def upload_path(self, filename):
        return os.path.basename(filename)

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    logo = models.ImageField(max_length=512, upload_to=upload_path)
    logo_alt = models.ImageField(max_length=512, upload_to=upload_path)
    level = models.CharField(max_length=64, choices=SponsorLevels.choices)
    link = models.URLField(blank=True)
