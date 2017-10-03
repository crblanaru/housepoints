from django.contrib import admin
from .models import HousePoints, AccademicYear
# Register your models here.

class HousePointsAdmin(admin.ModelAdmin):
    fields = ('firman','goodman', 'pantlin', 'displayyear', 'shortreason' ,'datesubmitted','submitby','deleted')
    list_display = ('firman','goodman', 'pantlin', 'displayyear', 'datesubmitted','submitby','deleted')


class AccademicYearAdmin(admin.ModelAdmin):
    fields = ('startdate', 'enddate', 'displayyear')
    list_display = ('startdate', 'enddate', 'displayyear')

admin.site.register(HousePoints, HousePointsAdmin)
admin.site.register(AccademicYear, AccademicYearAdmin)