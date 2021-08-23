
from trainer.models import Trainer
from django.shortcuts import render
from .forms import TrainersRegestrationForm

def register_trainers(request):
    if request.method=="POST":
        form=TrainersRegestrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainersRegestrationForm()
    return render(request,"register_trainers.html",{"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})


# Create your views here.
