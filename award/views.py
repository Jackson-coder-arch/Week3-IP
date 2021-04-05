from django.shortcuts import render
from .models import(
    Project,
    Profile,
)

def home(request):
    if request.method == 'GET':
        project = projects.objects.all()

    return render(request,'home.html',{'project':project})

def projects(request):
    if request.method == 'POST':

        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'projects.html',{'form':form})