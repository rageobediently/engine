from django.contrib import admin
from display.models import Metric, Sensor, Location

admin.site.register(Metric)
admin.site.register(Sensor)
admin.site.register(Location)
