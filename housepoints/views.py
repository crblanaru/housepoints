import csv

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models import Sum
from django.urls import reverse_lazy
from django.utils import timezone
from .models import HousePoints, get_current_year

# Create your views here.
class HomeView(TemplateView):
    """
    Index page
    """
    template_name = 'housepoints/home.j2'

    def get_context_data(self, **kwargs):
        valid_points = HousePoints.objects.filter(deleted=False, displayyear=get_current_year()).aggregate(pantlin=Sum('pantlin'), goodman=Sum('goodman'), firman=Sum('firman'))
        context = {'valid_points':valid_points}
        return context


class PointsInsert(CreateView):
    """
    Simple form to add points to the list
    """
    model = HousePoints
    fields = ['firman', 'goodman', 'pantlin', 'shortreason', 'submitby', 'displayyear']
    template_name = 'housepoints/addpoints.j2'
    success_url = reverse_lazy('housepoints:index')

class ViewAllNonDeleted(ListView):
    """
    View all non-deleted elements
    """
    queryset = HousePoints.objects.filter(deleted=False)
    context_object_name = 'housepoints'
    template_name = 'housepoints/nondeleted.j2'

def export_housepoints_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="allhousepointsrecords.csv"'

    writer = csv.writer(response)
    writer.writerow(['firman', 'goodman', 'pantlin', 'reason', 'submitby','date', 'academicyear'])

    items = HousePoints.objects.filter(deleted=False).values_list('firman', 'goodman', 'pantlin', 'shortreason', 'submitby', 'datesubmitted','displayyear')
    items = [(item[0], item[1], item[2], item[3], item[4], timezone.localtime(item[5]).strftime("%d/%m/%y %H:%M"), item[6]) for item in items]
    for item in items:
        writer.writerow(item)

    return response