from django.contrib import admin
from .models import Flight, Airport
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "city"]
    search_fields = ["code", "city"]
    ordering = ["city"]

admin.site.register(Flight, FlightAdmin)
# admin.site.register(Airport)