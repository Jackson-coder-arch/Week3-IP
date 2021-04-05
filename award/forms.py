from django import forms
from .models import Project, Profile, Rate, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pyuploadcare.dj.forms import ImageField



class ProjectForm(forms.ModelForm):

    class Meta:
        models = Project
        fields = ('name','image','description','link')

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'contact_info']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content', 'creativity']