from django.db import models
from django.contrib.gis.db import models

class Perangkat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    coordinates = models.PointField()
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perangkat'
        verbose_name_plural = 'Perangkat'

    def __str__(self):
        return self.name
    

class RiwayatPerangkat(models.Model):
    perangkat = models.ForeignKey(Perangkat, on_delete=models.CASCADE)
    coordinates = models.PointField()
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Riwayat Perangkat'
        verbose_name_plural = 'Riwayat Perangkat'
    
    def __str__(self):
        return "{} {}".format(self.perangkat.name, self.last_updated)