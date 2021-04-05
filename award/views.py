from django.shortcuts import render
from .models import(
    Project,
    Profile,
)

def home(request):
    if request.method == 'GET':
        post = Project.get_info()
        print(post)

    return render(request,'home.html',{'post':post})

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


def profile(request):
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES)
        if form.is_valid():
            form = profile.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = Profile()

    return render(request,'profile.html',{'form':form})