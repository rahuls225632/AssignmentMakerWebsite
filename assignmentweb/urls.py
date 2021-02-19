from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

from .views import home
from .views import register
from .views import login1
from .views import loginpage
from .views import newweb,newwebnavbar,about,form_info,activenewweb,logoutuser
urlpatterns = [
  
 path('',newweb, name="newweb"),
 path('newweb/login/',loginpage, name = 'login'),
 path('newweb/registernew/',register, name = 'register'),
 
 path('newwebnavbar',newwebnavbar),
 path('about',about,name="about"),
 path('newweb/forminfo',form_info, name="forminformation"),
 path('activenewweb',activenewweb,name='activenewweb'),
 path('logout',logoutuser,name='logoutuser')
]