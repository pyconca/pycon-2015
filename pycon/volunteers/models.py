from django.db import models

class Volunteer(models.Model):

    name = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    
    class Meta:
        app_label = "volunteers"
