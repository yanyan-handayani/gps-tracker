from django.shortcuts import render
from .models import Perangkat
from django.core.serializers import serialize
from django.conf import settings

def map_view(request):
    geojson = serialize('geojson', Perangkat.objects.all(), geometry_field='coordinates', fields=['name', 'last_updated'])
    return render(request, 'map.html', {'locations': geojson, 'LEAFLET_CONFIG': settings.LEAFLET_CONFIG})