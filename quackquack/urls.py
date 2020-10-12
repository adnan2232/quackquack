"""quackquack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import edit
from apps.core.views import frontpage,signup
from django.contrib.auth import views
from apps.feed.views import feed,search
from apps.conversation.views import conversations,conversation
from apps.quackerprofile.views import edit_profile, follow_quacker, quackerprofile,unfollow_quacker,followers,follows
from apps.feed.api import api_add_quack,api_add_like
from apps.conversation.api import api_add_message
from apps.notification.views import notifications

urlpatterns = [
    #
    #homepage
    path('',frontpage,name='frontpage'),
    #
    #signup
    path('signup/',signup,name='signup'),
    #
    #logout
    path('logout/',views.LogoutView.as_view(),name='logout'),
    #
    #login
    path('login/',views.LoginView.as_view(template_name='core/login.html'),name='login'),
    #
    #feed
    path('feed/',feed,name='feed'),
    #
    #search
    path('search/',search,name='search'),
    #
    #userprofile
    path('u/<str:username>/',quackerprofile,name='quackerprofile'),
    #
    #edit_profile
    path('edit_profile/',edit_profile,name="edit_profile"),
    #
    #follow
    path('u/<str:username>/follow/',follow_quacker,name='follow_quacker'),
    #
    #unfollow
    path('u/<str:username>/unfollow/',unfollow_quacker,name='unfollow_quacker'),
    #
    #followers
    path('u/<str:username>/followers',followers,name='followers'),
    #
    #follows
    path('u/<str:username>/follows',follows,name='follows'),
    #
    #conversations
    path('conversations/',conversations,name='conversations'),
    path('conversations/<int:user_id>/',conversation,name='conversation'),
    #
    #notifications
    path('notifications/',notifications,name='notifications'),
    #
    #api
    path('api/add_quack/',api_add_quack,name='api_add_quack'),
    path('api/add_like/',api_add_like,name="api_add_like"),
    path('api/add_message/',api_add_message,name="api_add_message"),
    #
    #admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
