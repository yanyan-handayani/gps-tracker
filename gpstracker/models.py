from django.db import models
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    coordinates = models.PointField()

    def __str__(self):
        return self.name