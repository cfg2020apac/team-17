from django.db import models

class Event (models.Model):
    event_title = models.CharField(max_length=200)
    event_content = models.TextField()
    event_published = models.DateTimeField('date published')

    def __str__(self):
        return self.event_title

