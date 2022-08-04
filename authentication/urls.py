
from django.contrib import admin
from django.urls import include,path
from . import views  #imported views

urlpatterns = [
    path('', views.home, name='home'), # So whenever a user requests this path ,he will be redirected to views.home function
    path('signup', views.signup, name='signup'), #signup function url
    path('teachersignup', views.teachersignup, name='teachersignup'),#teacherssignup url
    path('signin', views.signin, name='signin'),#signin url
    path('teachersignin', views.teachersignin, name='teachersignin'),#teachers signin url
    path('signout', views.signout, name='signout'), #signout url
    path('profile',views.profile,name='profile') #profile page url
    

]
  
'''
  check views.py to see all the functions there.
'''