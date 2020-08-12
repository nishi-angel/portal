from django.urls import path,include
from django.conf.urls import include, url
from django.contrib import admin
from . import views




from .views import (
	
    login_view,
    profile,
    register,
    auth,
    user_logout,
    edit_profile,
	)


urlpatterns = [
    path("", login_view, name = "login"),
    path('index/', views.index, name='index'),
    url(r"^profile/$", profile, name = "profile"),
    url(r"^register/$", register, name = "register"),
    url(r"^edit_profile/$", edit_profile, name= "edit_profile"),
    url(r"^logout/$", user_logout, name = "logout"),
    path("check_user/",views.check_user,name="check_user"),
    
   
    
   
    
    
]