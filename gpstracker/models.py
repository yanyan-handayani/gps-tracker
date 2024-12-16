from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# model untuk perangkat
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
    
# model untuk riwayat perangkat
class RiwayatPerangkat(models.Model):
    perangkat = models.ForeignKey(Perangkat, on_delete=models.CASCADE)
    coordinates = models.PointField()
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Riwayat Perangkat'
        verbose_name_plural = 'Riwayat Perangkat'
    
    def __str__(self):
        return "{} {}".format(self.perangkat.name, self.last_updated)
    


@receiver(post_save, sender=RiwayatPerangkat)
def update_parent_on_child_save(sender, instance, created, **kwargs):
    if created:  # Only update if a new child was created
        parent = instance.perangkat
        parent.last_updated = instance.last_updated  # Update a specific field, if necessary
        parent.save()