from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from api.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method=="GET":
        return render(request,'frontend/home.html')


def login(request):
    return render(request,'/api/login')


def register(request):
    if request.method=="GET":
        form=UserCreationForm()
        return render(request,'frontend/register.html',{'form':form})
@login_required
def blog(request):
    posts=Post.objects.filter(author=request.user)
    return render(request,'frontend/blog.html',{'posts':posts})
        