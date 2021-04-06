from django.urls import path,re_path
from django.contrib.auth import views

from .views import(
    home,
    projects,
    profile,
)


urlpatterns = [
    path('',home, name='home'),
    path('projects',projects, name='projects'),
    path('profile/',profile,name='profile')
]