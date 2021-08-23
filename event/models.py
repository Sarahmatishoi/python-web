from django.db import models
class Event(models.Model):
    event_name=models.CharField(max_length=16)
    day_of_event=models.DateField()
    event_venue=models.CharField(max_length=16)
    event_description=models.CharField(max_length=30)
    event_duration=models.DateField()
    event_link=models.CharField(max_length=30)
    attendees=models.CharField(max_length=20)
    email=models.EmailField()

# Create your models here.
