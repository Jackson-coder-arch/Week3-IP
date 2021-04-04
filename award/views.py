from django.shortcuts import render
from .models import(
    Project,
    Profile,
)

def home(request):
    projects = project.objects.all()
    context = {"project_list": projects}
    return render(request, 'home.html', context = context)

def project(request):
    project = get_object_or_404(Project,description= description, )
    return render(request, 'projects.html',{'project':project})