from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Course


# Create your views here.

def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    
    data={"students":students,"trainers":trainers,"courses":courses}
    return render(request,"homepage.html",data)
