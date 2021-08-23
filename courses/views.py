from courses.models import Course
from django.shortcuts import render
from django import forms
from .forms import CourseRegistrationForm


def register_course(request):
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseRegistrationForm()
    return render(request,"details_courses.html",{"form":form})


def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.html",{"courses":courses})


# Create your views here.
