from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    nationality=models.CharField
    
    
    


# Create your models here.
