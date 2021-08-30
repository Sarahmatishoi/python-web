from django import forms
from django.forms import ModelForm
from django.db import models
from.models import Event




class CalenderRegistrationForm(forms.ModelForm):
    class Meta:
        models=Event
        fields='__all__'

def __init__(self,*args,**kwargs):
    super(CalenderRegistrationForm,self).__init__(*args,**kwargs)
    self.fields['start_time'].input_formats('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats('%Y-%m-%dT%H:%M',)

