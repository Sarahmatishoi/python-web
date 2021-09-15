from django.db import models

class Trainer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=14)
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=20)
    image=models.ImageField()
    email=models.EmailField()
    Date_of_Birth=models.DateField()
    gender_choice=((u'M',u'Male'),(u'F',U'Female'),(u'O',u'Others'))
    gender=models.CharField(max_length=12,choices=gender_choice)
    subject_name=models.CharField(max_length=20)
    national_id=models.CharField(max_length=12)
    salary=models.PositiveBigIntegerField()
    phone_number=models.CharField(max_length=12)
    job_title=models.CharField(max_length=30)
    company=models.CharField(max_length=12)
    resume=models.FileField()

# Create your models here.
