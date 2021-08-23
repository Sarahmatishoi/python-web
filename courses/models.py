import trainer
from django.db import models
class Course(models.Model):
    course_name=models.CharField(max_length=12)
    course_code=models.CharField(max_length=6)
    trainer_id=models.CharField(max_length=10)
    course_description=models.CharField(max_length=16)
    course_channel=models.CharField(max_length=16)
    course_email=models.EmailField()
    
# Create your models here.
