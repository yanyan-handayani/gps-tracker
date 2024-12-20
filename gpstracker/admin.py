from django.contrib import admin
from gpstracker import models as m

class AdminPerangkat(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'description', 'coordinates', 'last_updated']
    readonly_fields = ['last_updated']
    
class AdminRiwayat(admin.ModelAdmin):
    search_fields = ['perangkat']
    list_display = ['perangkat', 'coordinates', 'last_updated']
    readonly_fields = ['last_updated']

admin.site.site_header  =  "Admin GPS Tracker"  
admin.site.site_title  =  "Admin GPS Tracker"
admin.site.index_title  =  "Admin GPS Tracker"

admin.site.register(m.Perangkat, AdminPerangkat)
admin.site.register(m.RiwayatPerangkat, AdminRiwayat)
