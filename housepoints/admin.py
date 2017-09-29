from django.contrib import admin
from .models import HousePoints
# Register your models here.

class HousePointsAdmin(admin.ModelAdmin):
    fields = ('firman','goodman', 'pantlin', 'datesubmitted','submitby','deleted')
    list_display = ('firman','goodman', 'pantlin', 'datesubmitted','submitby','deleted')

admin.site.register(HousePoints, HousePointsAdmin)