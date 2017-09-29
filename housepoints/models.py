from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class HousePoints(models.Model):
    """
    HousePoints(pantlin, firman, goodman, datesubmitted, submitby, deleted)
    """
    pantlin = models.PositiveIntegerField(verbose_name="Pantlin", validators=[MinValueValidator(0)], default=0)
    firman = models.PositiveIntegerField(verbose_name="Firman", validators=[MinValueValidator(0)], default=0)
    goodman = models.PositiveIntegerField(verbose_name="Goodman", validators=[MinValueValidator(0)], default=0)
    datesubmitted = models.DateTimeField(verbose_name="Date submitted", default=timezone.now)
    submitby = models.CharField(verbose_name="Submitted by", max_length=50)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return ("F: {}, G: {}, P:{} on {} by {}".format(
            self.firman,
            self.goodman,
            self.pantlin,
            self.datesubmitted,
            self.submitby
        ))