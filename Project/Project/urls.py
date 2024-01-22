"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.views import *


              
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage,name="homePageUrl"),
    path('studentPage', studentPage,name="studentPageUrl"),
    path('teacherPage', teacherPage,name="teacherPageUrl"),
    path('stuffPage',stuffPage,name="stuffPageUrl"),
    path('managementPage',managementPage,name="managementPageUrl"),
    path('libraryPage',libraryPage,name="libraryPageUrl"),
    path('',loginPage,name="loginPageUrl"),
    path('signupPage',signupPage,name="signupPageUrl"),
     path('logoutPage',logoutPage,name="logoutPage"),
    
    

    
    path('studentAdd',studentAdd,name="studentAdd"),
    path('teacherAdd',teacherAdd,name="teacherAdd"),
    path('stuffAdd',stuffAdd,name="stuffAdd"),
    path('managementAdd',managementAdd,name="managementAdd"),
    path('libraryAdd',libraryAdd,name="libraryAdd"),
    
    path('editStudent/<str:myid>',editStudent,name="editStudent"),
    path('deleteStudent/<str:myid>',deleteStudent,name="deleteStudent"),
    path('updateStudent',updateStudent,name="updateStudent"),
    
    path('editTeacher/<str:myid>',editTeacher,name="editTeacher"),
    path('deleteTeacher/<str:myid>',deleteTeacher,name="deleteTeacher"),
    path('updateTeacher',updateTeacher,name="updateTeacher"),
   
    path('editStuff/<str:myid>',editStuff,name="editStuff"),
    path('deleteStuff/<str:myid>',deleteStuff,name="deleteStuff"),
    path('updateStuff',updateStuff,name="updateStuff"),
    
    path('editmanagement/<str:myid>',editmanagement,name="editmanagement"),
    path('deletemanagement/<str:myid>',deletemanagement,name="deletemanagement"),
    path('updatemanagement',updatemanagement,name="updatemanagement"),
   
    
    path('editlibrary/<str:myid>',editlibrary,name="editlibrary"),
    path('deletelibrary/<str:myid>',deletelibrary,name="deletelibrary"),
    path('updatelibrary',updatelibrary,name="updatelibrary"),
    path('myprofile',myprofile,name="myprofile"),
    
    
    path ('myStudent/<str:myid>',Student,name="myStudent"),
    path ('Teacher/<str:myid>',Teacher,name="Teacher"),
     path ('Stuff',Stuff, name='Stuff'),     
    path ('Management',Management, name='Management'),
    path ('Library',Library, name='Library_List'), 
    
    
    path ('myStudent_List',Student_List, name='myStudent_List'),
    path ('Teacher_List',Teacher_List, name='Teacher_List'), 
    path ('Stuff_List',Stuff_List, name='Stuff_List'),     
    path ('Management_List',Management_List, name='Management_List'),
    path ('Library_List',Library_List, name='Library_List'), 
    
    
   
    
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)