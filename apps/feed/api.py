import json
import re
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Quack,Like
from apps.notification.utilities import create_notification

@login_required
def api_add_quack(request):
    data = json.loads(request.body)
    body = data['body']
    quack = Quack.objects.create(body=body, created_by = request.user)
    results = re.findall("(^|[^@\w])@(\w{1,20})",body)

    for result in results:
        result = result[1]
        print(result)

        if User.objects.filter(username=result).exists() and result!=request.user.username:
            create_notification(request,User.objects.get(username=result),'mention')

    return JsonResponse({'success':True})

@login_required
def api_add_like(request):
    data =json.loads(request.body)
    quack_id =  data['quack_id']
    if not Like.objects.filter(quack_id=quack_id).filter(created_by=request.user).exists():
        like = Like.objects.create(quack_id=quack_id,created_by = request.user)
        quack = Quack.objects.get(pk= quack_id)
        create_notification(request, quack.created_by,'like')
    
    return JsonResponse({'success':True})