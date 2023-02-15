from django.db import models

from django.db.models.fields.files import ImageField

class Programate_projects(models.Model):
    title = models.CharField(max_length= 100)
    description = models.CharField(max_length= 100)
    image = ImageField (upload_to="portfolio/img/")
    link = models.URLField(blank= True)
