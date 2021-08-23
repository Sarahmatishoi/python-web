from django import forms
from django.db import models
from django.forms import ModelForm, fields
from.models import Course

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"