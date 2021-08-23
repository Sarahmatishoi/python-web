from student.models import Student
from django import forms
from django.shortcuts import render
from .forms import StudentRegestrationForm
from .models import Student


# Create your views here.
def register_student(request):
    form=StudentRegestrationForm()
    return render(request,"register_student.html",{"form":form})

def register_student(request):
    if request.method == "POST":
        form=StudentRegestrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegestrationForm()
    return render(request,"register_student.html",{"form":form})
def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})

