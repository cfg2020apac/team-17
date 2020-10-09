from django.db import models

# Create your models here.
class PointRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    point = models.IntegerField()
    time = models.DateTimeField()
