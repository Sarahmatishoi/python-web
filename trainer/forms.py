from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Trainer

class TrainersRegestrationForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"
