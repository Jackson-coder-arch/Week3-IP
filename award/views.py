from django.shortcuts import render
from .models import(
    Project,
    Profile,
)

def home(request):
    project = projects.objects.all()
    context = {"project_list": project}
    return render(request, 'home.html', context = context)

def projects(request):
    projects = get_object_or_404(Projects,description= description, )
    return render(request, 'projects.html',{'project':project})