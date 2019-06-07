from django.db import models
from .survey import Survey


class Queues(models.Model):
    name = models.CharField(max_length=240, db_index=True)
    survey = models.ForeignKey(Survey, db_index=True, on_delete=models.CASCADE)


