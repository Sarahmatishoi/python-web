from trainer.models import Trainer
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from courses.models import Course
from calender.models import Event



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name","course_code","course_description")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("title","description","start_time","end_time")

