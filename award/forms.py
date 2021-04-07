from django import forms
from django.forms import ModelForm
from .models import Project, Profile, Rating, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name','image','description','link')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content', 'creativity']