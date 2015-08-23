from django.db import models


class Mailing(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
