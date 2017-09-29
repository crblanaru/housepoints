from django.views.generic.edit import CreateView
from .models import HousePoints

class PointsInsert(CreateView):
    """
    Simple form to add points to the list
    """
    model = HousePoints