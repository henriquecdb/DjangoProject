from medicSearch.models import *


class DayWeek(models.Model):
    name = models.CharField(null=False, max_length=20)
