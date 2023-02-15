from django.db import models

from django.db.models.fields.files import ImageField

class Tech(models.Model):
    name = models.CharField(max_length= 100)
    icon = models.FileField(upload_to="portfolio/icons/")

