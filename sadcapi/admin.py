from django.contrib import admin
from .models import CountryData, ThematicArea
# Register your models here.
admin.site.register(ThematicArea)
admin.site.register(CountryData)