from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import ProjectForm, RegistrationForm, UpdateUserProfileForm
# from .serializers import projectSerializer
# from django.contrib.auth.decorators import login_required

from .models import(
    Project,
    Profile,
    Rating,
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
            form = UpdateUserProfileForm.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = UpdateUserProfileForm()

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
        form = RegistrationForm()
    return render(request, 'django_registration/registration_form.html',{'form':form} )

def rate(request):
    ratings = Rate.objects.all()
    rate_params = {
        'ratings': ratings
    }

class ProjectList(APIView):
    def get(self, request):
        project1 =Project.objects.all()
        serializer = ProjectSerializer(project1,many=True)
        return Response(serializer.data)


    def post(self): 
        pass



def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            
            if user is not None:   
                login(request, user)
               
        context={}
        return render(request,'registration/login.html',  context)

def logout(request):
    logout(request)
    return redirect('login')  

def search_project(request):
    if 'name' in request.GET and request.GET['name']:
        search_term = request.GET.get("name")
        searched_posts = Posts.search_by_posts(search_term)
        
        message = f'{search_term}'
    else:
        message = "You haven't searched for any term"
    
    return render(request,'search.html')
    
    context={
        "message": message,
        "posts":searched_posts
    }    
        
    return render(request,'search.html',context)
 