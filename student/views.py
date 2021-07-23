from django import forms
from django.shortcuts import render
from .forms import StudentRegestrationForm

# Create your views here.
def register_student(request):
    form=StudentRegestrationForm()
    return render(request,"register_student.html",{"form":form})
