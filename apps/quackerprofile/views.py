
from django.http import request
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from apps.feed.models import Quack
from django.contrib.auth.decorators import login_required
from .forms import QuackerProfileForm
from apps.notification.utilities import create_notification

def quackerprofile(request,username):
    user = get_object_or_404(User, username=username)
    quacks = Quack.objects.filter(created_by = user)
    qquacks = quacks.all()
    for quack in qquacks:
        likes = quack.likes.filter(created_by_id=request.user.id)
        if likes.count()>0:
            quack.liked=True
        else:
            quack.liked = False
    context = {
        'user':user,
        'quacks':quacks,
        'qquacks':qquacks,
    }
    return render(request,'quackerprofile/quackerprofile.html',context)

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = QuackerProfileForm(request.POST,request.FILES,instance=request.user.quackerprofile)

        if form.is_valid():
            form.save()
            return redirect('quackerprofile',username=request.user.username)
    else:
        form = QuackerProfileForm(instance=request.user.quackerprofile)
    context = {
        'user':request.user,
        'form':form
    }
    return render(request,'quackerprofile/edit_profile.html',context)

@login_required
def follow_quacker(request,username):
    user = get_object_or_404(User,username=username)
    request.user.quackerprofile.follows.add(user.quackerprofile)
    create_notification(request, user,'follower')
    return redirect('quackerprofile',username=username)

@login_required
def unfollow_quacker(request,username):
    user = get_object_or_404(User,username=username)
    request.user.quackerprofile.follows.remove(user.quackerprofile)
    return redirect('quackerprofile',username=username)

def followers(request,username):
    user = get_object_or_404(User,username=username)
    context = {
        'user':user
    }
    return render(request,'quackerprofile/followers.html',context)

def follows(request,username):
    user = get_object_or_404(User,username=username)
    context = {
        'user':user
    }
    return render(request,'quackerprofile/follows.html',context)