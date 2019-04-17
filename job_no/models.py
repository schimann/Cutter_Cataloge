from django.db import models

from django.conf import settings

class JobNo(models.Model):
    job_no = models.IntegerField(default=0)
