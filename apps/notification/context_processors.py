from django.db import reset_queries
from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        return{'notifications':request.user.notifications.filter(is_read=False)}
    else:
         return{'notifications':[]}