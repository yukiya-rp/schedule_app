from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title