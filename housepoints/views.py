from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.db.models import Sum
from django.urls import reverse_lazy
from .models import HousePoints

# Create your views here.
def index(request):
    """
    Index page
    """
    valid_points = HousePoints.objects.filter(deleted=False).aggregate(pantlin=Sum('pantlin'), goodman=Sum('goodman'), firman=Sum('firman'))
    context = {'valid_points':valid_points}
    return render(request, 'housepoints/index.html', context)

class PointsInsert(CreateView):
    """
    Simple form to add points to the list
    """
    model = HousePoints
    fields = ['firman', 'goodman', 'pantlin', 'submitby']
    template_name = 'housepoints/addpoints.html'
    success_url = reverse_lazy('housepoints:index')