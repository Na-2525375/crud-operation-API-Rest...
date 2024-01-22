from django.contrib import admin

# Register your models here.

from App.models import Students_Model
from App.models import Teacher_Model
from App.models import Stuff_Model
from App.models import Management_Model
from App.models import Library_Model

class Students_Model_Display(admin.ModelAdmin):
    
    list_display=['First_Name', 'Last_Name', 'Mobile','Email','Age']
    
admin.site.register(Students_Model,Students_Model_Display)
    
class Teacher_Model_Display(admin.ModelAdmin):
    
    list_display=['First_Name', 'Last_Name', 'Mobile','Email','Age']
    
admin.site.register(Teacher_Model,Teacher_Model_Display)

class  Stuff_Model_Display(admin.ModelAdmin):

    list_display=['First_Name', 'Last_Name', 'Mobile','Email','Age']
 
admin.site.register(Stuff_Model,Stuff_Model_Display)
 
class Management_Model_Display(admin.ModelAdmin):
   
   list_display=['First_Name', 'Last_Name', 'Mobile','Email','Age']
 
admin.site.register(Management_Model,Management_Model_Display) 

class Library_Model_Display(admin.ModelAdmin):



 list_display=['Book_Name', 'Writer_Name', 'Serial_No','Acquisition_Date','Return_Date']

admin.site.register(Library_Model,Library_Model_Display)