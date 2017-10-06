from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AccademicYear(models.Model):
    """
    Results should be displayed per year
    """
    startdate = models.DateField(verbose_name="Start Date")
    enddate = models.DateField(verbose_name="End Date")
    displayyear = models.PositiveIntegerField(verbose_name="Display Year", validators=[MinValueValidator(2000)])

    def __str__(self):
        return(str(self.displayyear))

    class Meta:
        ordering = ['-displayyear']


def get_current_year():
    now = timezone.now()
    return AccademicYear.objects.filter(startdate__lte=now, enddate__gte=now)


class HousePoints(models.Model):
    """
    HousePoints(pantlin, firman, goodman, datesubmitted, submitby, deleted)
    """
    pantlin = models.PositiveIntegerField(verbose_name="Pantlin", validators=[MinValueValidator(0)], default=0)
    firman = models.PositiveIntegerField(verbose_name="Firman", validators=[MinValueValidator(0)], default=0)
    goodman = models.PositiveIntegerField(verbose_name="Goodman", validators=[MinValueValidator(0)], default=0)
    shortreason = models.CharField(verbose_name="Reason", max_length=100, default='')
    datesubmitted = models.DateTimeField(verbose_name="Date submitted", default=timezone.now)
    displayyear = models.ForeignKey(AccademicYear, on_delete=models.PROTECT, verbose_name="Academic Year", default=get_current_year())
    submitby = models.CharField(verbose_name="Submitted by", max_length=50)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return ("Points inserted on {} by {}".format(
            self.datesubmitted,
            self.submitby
        ))
    
    def clean(self):
        if self.pantlin + self.firman + self.goodman == 0:
            raise ValidationError(_('You must enter at least one non-zero value.'))

        if self.pantlin < 0 or self.goodman < 0 or self.firman < 0:
            raise ValidationError(_('You are not allowed negative points.'))
