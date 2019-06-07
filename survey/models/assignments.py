from django.db import models
from .queues import Queues

class Assignments(models.Model):


    queue_id = models.ForeignKey(Queues, db_index=True, on_delete=models.CASCADE)
    alert_id = models.CharField(max_length=240, db_index=True)
    user_id = models.IntegerField(default=9999)
    completed = models.BooleanField(default=False)