from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

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
    # if request.method == 'POST':

    #     form = ProjectForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print('form is valid')
    #         post = form.save(commit=False)
    #         post.save()
    #         return redirect('home')
    # else:
    #     form = ProjectForm()

    return render(request, 'projects7.html',{'form':form})


def profile(request):
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES)
        if form.is_valid():
            form = profile.save(commit=False)
            # form.user = user
            form.save()
            return redirect('home')
    else:
        form = Profile()

    return render(request,'profile.html',{'form':form})

def registration(request):
    if request.method =='POST':
            form = UserCreationForm()
            context = {'form':form}
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'django_registration/registration_form',{'form':form} )

