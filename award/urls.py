from django.urls import path,re_path
from django.contrib.auth import views
# from rest_work.urlpatterns import formart_suffix_patterns
from .views import(
    home,
    projects,
    profile,
    search_project,
    login,
    registration,
    logout,
)


urlpatterns = [
    path('',home, name='home'),
    path('projects/',projects, name='projects'),
    path('registration/',registration, name= 'registration'),
    path('login/',login,name='login'),
    path('logout/',logout, name='logout'),
    path('profile/',profile,name='profile'),
    path('search/',search_project,name ='search'),
]