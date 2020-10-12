from django.db import models
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quack,Like
from django.contrib.auth.models import User

@login_required
def feed(request):
    userids = [request.user.id]
    for quacker in request.user.quackerprofile.follows.all():
        userids.append(quacker.user.id)
    quacks = Quack.objects.filter(created_by_id__in=userids)
    for quack in quacks:
        likes = quack.likes.filter(created_by_id=request.user.id)
        if likes.count()>0:
            quack.liked=True
        else:
            quack.liked = False
    context = {
        'quacks':quacks
    }
    return render(request,'feed/feed.html',context)
@login_required
def search(request):
    query = request.GET.get('query','')
    if len(query)>0:
        quackers = User.objects.filter(username__icontains=query)
        quacks= Quack.objects.filter(body__icontains=query)
    else:
        quackers = []
        quacks =[]
    context ={
        'query':query,
        'quackers':quackers,
        'quacks':quacks,
    }
    return render(request,'feed/search.html',context)
