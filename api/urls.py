"""InnoClubs URL Configuration

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
from django.urls import path

from . import views


urlpatterns = [
    path('get_auth_url/', views.get_auth_url, name='get-auth-url'),
    path('microsoft/login/', views.OutlookLogin.as_view(), name='user-login'),

    path('user_info/<str:email>/', views.UserInfoRUView.as_view(), name='user-info'),

    path('create_club/', views.CreateClubView.as_view(), name='club-create')  # why all users are present after creation?
    # get all clubs
    # join club
    # change header of the club
    # retrieve, update and destroy club
]
