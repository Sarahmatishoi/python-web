
from trainer.models import Trainer
from django.shortcuts import redirect, render
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



def edit_trainer(request,id):
    trainers=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainersRegestrationForm(request.POST,instance=trainers)
        if form.is_valid():
            form.save()
    else:form=TrainersRegestrationForm(instance=trainers)
    return render(request,"edit_trainer.html",{"form":form})

def trainer_profile(request,id):
    trainers=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainers":trainers})

def delete_trainer(request,id):
    trainers=Trainer.objects.get(id=id)
    trainers.delete()
    return redirect("trainer_list")


# Create your views here.
