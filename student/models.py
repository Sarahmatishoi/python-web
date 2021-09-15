from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(null=True)
    nationality_choice=((u'k',u'Kenyan'),(u'u',u'Ugandan'),(u'R',u'Rwandan'),(u'S',u'Sudanese'),(u'S',u'SouthSudanese'))
    nationality=models.CharField(max_length=20,choices=nationality_choice)
    image=models.ImageField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    gender_choice=((u'F',u'Female'),(u'm',u'Male'),(u'O','Other'))
    gender=models.CharField(max_length=16,choices=gender_choice)
    subject=models.CharField(max_length=30,null=True,blank=True)
    health_records=models.FileField()
    class_room=models.CharField(max_length=16,null=True,blank=True)
    phone_number=models.CharField(max_length=12,null=True,blank=True)
    gurdian_name=models.CharField(max_length=20,null=True,blank=True)
    gurdian_contact=models.CharField(max_length=12,null=True,blank=True)
    parent_name=models.CharField(max_length=20,null=True,blank=True)
    parent_contact=models.CharField(max_length=12,null=True,blank=True)
    passport=models.CharField(max_length=20,null=True,blank=True)
    academic_year=models.DateField(max_length=8,blank=True,null=True)
    admission_date=models.DateField(max_length=16,null=True,blank=True)
    languages_choice=((u'E',u'English'),(u'K',u'Kiswahili'),(u'F',u'French'))
    languages=models.CharField(max_length=15,choices=languages_choice)



    
    


# Create your models here.
