from django.contrib import admin
from .models import Node, Activity, Sensor

# Register your models here.
admin.site.register(Node)
admin.site.register(Activity)
admin.site.register(Sensor)
