from django.db import models

from django.conf import settings

class Cutter(models.Model):
    cutter_name = models.CharField(max_length=50, primary_key=True)
#    job_no = models.IntegerField(default=0)
    cutter_id = models.IntegerField(default=0)
    cutter_in_draw = models.IntegerField(default=0)
    add_cutter =  models.IntegerField(default=0)
    sub_cutter = models.IntegerField(default=0)


def __str__(self):
    return self.cutter_name
