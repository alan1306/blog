from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def registerUser(request):
    form=UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('frontend:home')
    return render(request,'frontend/register.html',{'form':form})


@login_required
def searchUser(request):
    searched=request.POST["searchedName"]
    user=User.objects.filter(username=searched)
    posts=Post.objects.filter(author=user.first()).filter(public=True)
    return render(request,'frontend/blog.html',{'posts':posts})

@login_required
def createBlog(request):
    if request.method=="GET":
        form=PostForm()
        return render(request,'frontend/create-blog.html',{'form':form})
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('frontend:blog')
        else:
            return render(request,'frontend/create-blog.html',{'form':form})