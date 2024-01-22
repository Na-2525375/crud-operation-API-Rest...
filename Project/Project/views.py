from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from App.serializers import *
from App.models import *



def Student(request,myid):
    
    student=Students_Model.objects.get(id=myid)
    
    Serializer_Data=Students_Serializer(student)
    
    json_data= JSONRenderer().render(Serializer_Data.data)
    
    return HttpResponse(json_data,content_type="application/json")

def Student_List(request):
    student=Students_Model.objects.all()
    Student_Serializer_Data=Students_Serializer(student,many=True)
    
    
    return JsonResponse(Student_Serializer_Data.data, safe=False)
  
  
def Teacher(request,myid):
    
    Teacher=Teacher_Model.objects.get(id=myid)
    
    Serializer_Data=Teacher_Serializer(Teacher)
    
    json_data= JSONRenderer().render(Serializer_Data.data)
    
    return HttpResponse(json_data,content_type="application/json")

def Teacher_List(request):
    Teacher=Teacher_Model.objects.all()
    Teacher_Serializer_Data=Teacher_Serializer(Teacher,many=True)
    
    
    return JsonResponse(Teacher_Serializer_Data.data, safe=False)

def Stuff(request,myid):
    
    Stuff=Stuff_Model.objects.get(id=myid)
    
    Serializer_Data=Stuff_Model(Stuff)
    
    json_data= JSONRenderer().render(Serializer_Data.data)
    
    return HttpResponse(json_data,content_type="application/json")

def Stuff_List(request):
    Stuff=Stuff_Model.objects.all()
    Stuff_Serializer_Data=Teacher_Serializer(Stuff,many=True)
    
    
    return JsonResponse(Stuff_Serializer_Data.data, safe=False)  

def Management(request,myid):
    
    Management=Management_Model.objects.get(id=myid)
    
    Serializer_Data=Management_Model(Management)
    
    json_data= JSONRenderer().render(Serializer_Data.data)
    
    return HttpResponse(json_data,content_type="application/json")

def Management_List(request):
    Management=Management_Model.objects.all()
    Management_Serializer_Data=Management_Serializer(Management,many=True)
    
    
    return JsonResponse(Management_Serializer_Data.data, safe=False) 

def Library(request,myid):
    
    Library=Library_Model.objects.get(id=myid)
    
    Serializer_Data=Library_Model(Library)
    
    json_data= JSONRenderer().render(Serializer_Data.data)
    
    return HttpResponse(json_data,content_type="application/json")

def Library_List(request):
    Library=Library_Model.objects.all()
    Library_Serializer_Data=Library_Serializer(Library,many=True)
    
    
    return JsonResponse(Library_Serializer_Data.data, safe=False) 

   
#page
@login_required
def homePage(request):
    student=Students_Model.objects.filter(Marks__gt = 70)
    teacher=Teacher_Model.objects.all()
    stuff=Stuff_Model.objects.all()
    management=Management_Model.objects.all()
    library=Library_Model.objects.all()
    
    return render(request,"home.html",{"student":student, "teacher":teacher, "stuff":stuff,"management":management,"library":library})
    
    

def logoutPage(request):
    
    logout(request)
    
    return redirect("loginPageUrl")

def loginPage(request):
     myMessage={
        'Password_Error':'User Not Found',
        'Password_Success':'Login Successfully',
    }
    
     if request.method=="POST":

       user_name=request.POST.get("username")
       myPassword=request.POST.get("pass")
       
       print(user_name,myPassword)
       
       user=authenticate(request,username=user_name,password=myPassword)
       if user is not None:
           login(request,user)
           return redirect("homePageUrl")
       else:
           messages.warning(request,myMessage["Password_Error"])
           
       print(user)
    
     return render(request,"login.html")
 
def signupPage(request):
    
    myMessage={
        'Password_Error':'Password and Confirm Password Not Match',
        'Password_Success':'User Create Successfully',
    }
    if request.method=="POST":

       auth_name=request.POST.get("username")
       myemail=request.POST.get("email")
       pass1=request.POST.get("password1")
       pass2=request.POST.get("password2")
       
       if pass1!=pass2:
           messages.error(request,myMessage['Password_Error'])
       else:
           myuser=User.objects.create_user(auth_name,myemail,pass2)
           
           myuser.save()
           
           messages.success(request,myMessage['Password_Success'])
           
           return redirect("loginPageUrl")
       
    return render(request,"signup.html")

@login_required
def myprofile(request):
   return render(request,"myprofile.html")


@login_required
def studentPage(request):
    student = Students_Model.objects.all()

    context={
        "std":student,
    }

    return render(request,"student.html",context)

@login_required
def teacherPage(request):

    teacher = Teacher_Model.objects.all()

    context={
        "tch":teacher,
    }

    return render(request,"teacher.html",context)

@login_required
def stuffPage(request):

    stuff = Stuff_Model.objects.all()

    context={
        "emp":stuff,
    }

    return render (request,"stuff.html",context)

@login_required
def managementPage(request):

    management = Management_Model.objects.all()

    context={
        "auth":management,
    }

    return render(request,"management.html",context)

@login_required
def libraryPage(request):

    library = Library_Model.objects.all()

    context={
        "lib":library,
    }

    return render(request,"library.html",context)




#Student Page
@login_required
def studentAdd(request):
    
    my_Message= {
        'Error_Message':'Student Add Failed',
        'Success_Message':'Student Add Successfully',
    }

    if request.method=="POST":

       f_name=request.POST.get("firstname")
       l_name=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       Marks=request.POST.get("Marks")
       Profile_pic=request.FILES.get("Profile_pic")

       student=Students_Model(
        First_Name=f_name,
        Last_Name=l_name,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        Marks=Marks,
        
        myImage=Profile_pic

       )
       
       if Profile_pic:
           student.myImage=Profile_pic
       else:
           student.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
              
       student.save()
       
       messages.success(request,my_Message["Success_Message"])
       return redirect("studentPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        
        return redirect("studentPageUrl")

   

#Teacher Page
@login_required
def teacherAdd(request):
    
    my_Message= {
        'Error_Message':'Teacher Add Failed',
        'Success_Message':'Teacher Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        teacher=Teacher_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
         teacher.myImage=Profile_pic
        else:
           teacher.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
            
        teacher.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("teacherPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])

        return redirect("teacherPageUrl")

   

#Employee Page
@login_required
def stuffAdd(request):
    
    my_Message= {
        'Error_Message':'Employee Add Failed',
        'Success_Message':'Employee Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        stuff=Stuff_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
           stuff.myImage=Profile_pic
        else:
          stuff.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        stuff.save()
        
        messages.success(request,my_Message["Success_Message"])
        return redirect("stuffPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
            
        return redirect("stuffPageUrl")

   


#Authority Page
@login_required
def managementAdd(request):
    my_Message= {
        'Error_Message':'Authority Add Failed',
        'Success_Message':'Authority Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        management=Management_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           management.myImage=Profile_pic
        else:
          management.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        management.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("managementPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        
        return redirect("managementPageUrl")

    

#Library Page
@login_required
def libraryAdd(request):
    
    my_Message= {
        'Error_Message':'Library Add Failed',
        'Success_Message':'Library Add Successfully',
    }

    if request.method=="POST":

        b_name=request.POST.get("Book_Name")
        w_name=request.POST.get("Writer_Name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")
        Profile_pic=request.FILES.get("Profile_pic")
        library=Library_Model(
            Book_Name=b_name,
            Writer_Name=w_name,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           library.myImage=Profile_pic
        else:
           library.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        library.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("libraryPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        
        return redirect("libraryPageUrl")

    

@login_required
def editStudent(request,myid):
    student=Students_Model.objects.filter(id=myid)
    
    context={
        "student":student,
             }
    
    return render(request,"editStudent.html",context)
@login_required
def deleteStudent(request,myid):
    student=Students_Model.objects.filter(id=myid)
    student.delete()
    
    return redirect("studentPageUrl")
@login_required
def updateStudent(request):
    
    my_Message= {
        'Error_Message':'Student Add Failed',
        'Success_Message':'Student Add Successfully',
    }

    if request.method=="POST":
       studentid=request.POST.get("studentid")
       f_name=request.POST.get("firstname")
       l_name=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       Marks=request.POST.get("Marks")
       Profile_pic=request.FILES.get("Profile_pic")
       student=Students_Model(
        id=studentid,                    
        First_Name=f_name,
        Last_Name=l_name,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        Marks=Marks,
        myImage=Profile_pic
       )
         
       if Profile_pic:
           student.myImage=Profile_pic
       else:
           student.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
              
       student.save()
       
       messages.success(request,my_Message["Success_Message"])
       return redirect("studentPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        

    return redirect("studentPageUrl")

  
@login_required
def editTeacher(request,myid):
    teacher=Teacher_Model.objects.filter(id=myid)
    context={
        "teacher":teacher,
             }
    
    
    return render(request,"editteacher.html",context)

@login_required
def deleteTeacher(request,myid):
    teacher=Teacher_Model.objects.filter(id=myid)
    
    teacher.delete()
    
    return redirect("teacherPageUrl")

@login_required
def updateTeacher(request):
    my_Message= {
        'Error_Message':'Teacher Add Failed',
        'Success_Message':'Teacher Add Successfully',
    }

    if request.method=="POST":
        teacherid=request.POST.get("teach")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        teacher=Teacher_Model(
            id= teacherid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
         teacher.myImage=Profile_pic
        else:
           teacher.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
            
        teacher.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("teacherPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
       

        return redirect("teacherPageUrl")
    
@login_required    
def editStuff(request,myid):
    
   
      
    stuff=Stuff_Model.objects.filter(id=myid)
    
    
    context={
        "stuff":stuff,
             }
    
    
    return render(request,"editstuff.html",context)

@login_required 
def deleteStuff(request,myid):
    stuff=Stuff_Model.objects.filter(id=myid)
    
    stuff.delete()
    
    return redirect("stuffPageUrl")
@login_required 
def updateStuff(request):
    
    my_Message= {
        'Error_Message':'Employee Add Failed',
        'Success_Message':'Employee Add Successfully',
    }

    if request.method=="POST":
        employeeid=request.POST.get("emm")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        stuff=Stuff_Model(
            id=employeeid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           stuff.myImage=Profile_pic
        else:
           stuff.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        stuff.save()
        
        messages.success(request,my_Message["Success_Message"])
        return redirect("stuffPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
           
        return redirect("stuffPageUrl")
    
@login_required 
def editmanagement(request,myid):
    management=Management_Model.objects.filter(id=myid)
    
    
    context={
        "management":management,
             }
    
    
    return render(request,"editmanagement.html",context)
@login_required 
def deletemanagement(request,myid):
    management=Management_Model.objects.filter(id=myid)
    
    management.delete()
    
    return redirect("managementPageUrl")

@login_required 
def updatemanagement(request):
    my_Message= {
        'Error_Message':'Authority Add Failed',
        'Success_Message':'Authority Add Successfully',
    }

    if request.method=="POST":
        Authorityid=request.POST.get("aut")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        management=Management_Model(
            id=Authorityid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
           management.myImage=Profile_pic
        else:
          management.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        management.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("managementPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        

        return redirect("managementPageUrl")
@login_required    
def editlibrary(request,myid):
        
    library=Library_Model.objects.filter(id=myid)
    
    
    context={
        "library":library,
             }
    
    
    return render(request,"editlib.html",context)
@login_required 
def deletelibrary(request,myid):
    library=Library_Model.objects.filter(id=myid)
    
    library.delete()
    
    return redirect("libraryPageUrl")
@login_required 
def updatelibrary(request):
    
     
    my_Message= {
        'Error_Message':'Library Add Failed',
        'Success_Message':'Library Add Successfully',
    }


    if request.method=="POST":

        b_name=request.POST.get("Book_Name")
        w_name=request.POST.get("Writer_Name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")
        Profile_pic=request.FILES.get("Profile_pic")
        library=Library_Model(
            Book_Name=b_name,
            Writer_Name=w_name,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,
            myImage=Profile_pic
            )
        if Profile_pic:
           library.myImage=Profile_pic
        else:
           library.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        library.save()
        messages.success(request,my_Message["Success_Message"])
        return redirect("libraryPageUrl")
    else:
        messages.success(request,my_Message["Error_Message"])
        
       
        return redirect("libraryPageUrl")

    
