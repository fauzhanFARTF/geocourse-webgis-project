# from django.contrib import admin      @#Admin Non Spatial
from django.contrib.gis  import admin   # Admin Spatial
from .models import Facility

# Register your models here.
class LocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    default_lon = 18409015.29
    default_lat = 1300740.59

@admin.register(Facility)
class FacilityAdmin(LocationAdmin):
    list_filter = ['status', 'operator'] 
    list_display = ['id', 'name', 'status', 'operator']

# admin.site.register(Facility)
# class FacilityAdmin(LocationAdmin):
#     list_filter = ['status', 'operator']
#     list_display = ['id', 'name', 'status', 'operator']