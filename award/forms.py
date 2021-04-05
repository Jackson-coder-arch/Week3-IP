from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        models = Project
        fields = ('name','image','description','link')