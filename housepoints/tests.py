from django.test import TestCase
from .models import AccademicYear, HousePoints
from django.utils import timezone
from django.core.exceptions import ValidationError

class HousePointsTest(TestCase):

    new_accademic_year = AccademicYear(startdate=timezone.now(), enddate=timezone.now(), displayyear=2014)
    new_accademic_year.save()

    def test_zeros_as_points(self):
        """
        Testing insertion of points where sum is zero as it makes no sense to add them
        """
        h = HousePoints(pantlin=0,goodman=0,firman=0,shortreason='',displayyear=self.new_accademic_year, submitby='test')
        self.assertRaises(ValidationError, h.clean)

    def test_negative_as_points(self):
        """
        Testing insertion of points where sum is zero as it makes no sense to add them
        """
        h = HousePoints(pantlin=-10,goodman=-10,firman=-10,shortreason='',displayyear=self.new_accademic_year, submitby='test')
        self.assertRaises(ValidationError, h.clean)
    