from calender.models import Event
from django.shortcuts import render
from rest_framework import serializers, viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Course
from calender.models import Event
from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer, EventSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer


# Create your views here.
