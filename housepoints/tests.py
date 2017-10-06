"""
Test cases for the housepoints module
"""
from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import AccademicYear, HousePoints


class HousePointsTest(TestCase):
    """
    House Points Test Class
    """

    new_accademic_year = AccademicYear(
        startdate=timezone.now(),
        enddate=timezone.now(),
        displayyear=2014
        )
    new_accademic_year.save()

    def test_zeros_as_points(self):
        """
        Testing insertion of points where sum is zero as it makes no sense to add them
        """
        new_record = HousePoints(
            pantlin=0,
            goodman=0,
            firman=0,
            shortreason='',
            displayyear=self.new_accademic_year,
            submitby='test'
            )
        self.assertRaises(ValidationError, new_record.clean)

    def test_negative_as_points(self):
        """
        Testing insertion of points where sum is zero as it makes no sense to add them
        """
        new_record = HousePoints(
            pantlin=-10,
            goodman=-10,
            firman=-10,
            shortreason='',
            displayyear=self.new_accademic_year,
            submitby='test'
            )
        self.assertRaises(ValidationError, new_record.clean)

class AccademicYearTests(TestCase):
    """
    Accademic Year Test Class
    """
    def test_logic_start_and_end_date(self):
        """
        Testing that you cannot add an end date the start date
        """
        new_accademic_year = AccademicYear(
            startdate=timezone.now(),
            enddate=timezone.now() + timedelta(-1),
            displayyear=2014
            )
        self.assertRaises(ValidationError, new_accademic_year.clean)

    def test_overlap_in_accademic_year(self):
        """
        Testing that you cannot create overlapping dates ranges
        """
        fist_accademic_year = AccademicYear(
            startdate=timezone.now(),
            enddate=timezone.now() + timedelta(30),
            displayyear=2014
            )
        fist_accademic_year.save()
        new_accademic_year = AccademicYear(
            startdate=timezone.now() + timedelta(1),
            enddate=timezone.now() + timedelta(31),
            displayyear=2015
            )
        self.assertRaises(ValidationError, new_accademic_year.clean)
