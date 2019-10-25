from django.contrib import admin
from Places.models import Places,PlaceImage
# Register your models here.

class PlaceModelAdmin(admin.ModelAdmin):
    class Meta:
        model=Places


admin.site.register(Places, PlaceModelAdmin)
admin.site.register(PlaceImage) 