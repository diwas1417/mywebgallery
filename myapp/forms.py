from django import forms
from django.forms import fields, models
from .models import Image

class Imageforms(models.ModelForm):
    class Meta:
        model= Image
        fields="__all__"
        labels={'photo':''}