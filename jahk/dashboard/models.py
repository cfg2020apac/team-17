from django.db import models

# Create your models here.
class Course(models.Model):
    intro = models.CharField(max_length = 500)
    duration = models.DurationField()
    points = models.IntegerField()
    instructor = models.CharField(max_length = 100)
