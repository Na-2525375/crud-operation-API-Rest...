from rest_framework import serializers


class Students_Serializer(serializers.Serializer):
    First_Name=serializers.CharField(max_length=100)
    Last_Name=serializers.CharField(max_length=100)
    Mobile=serializers.CharField(max_length=100)
    Email=serializers.CharField(max_length=100)
    Age=serializers.CharField(max_length=100)
   
   

    
class Teacher_Serializer(serializers.Serializer):
    First_Name=serializers.CharField(max_length=100)
    Last_Name=serializers.CharField(max_length=100)
    Mobile=serializers.CharField(max_length=100)
    Email=serializers.CharField(max_length=100)
    Age=serializers.CharField(max_length=100)
    
    
class Stuff_Serializer(serializers.Serializer):
    First_Name=serializers.CharField(max_length=100)
    Last_Name=serializers.CharField(max_length=100)
    Mobile=serializers.CharField(max_length=100)
    Email=serializers.CharField(max_length=100)
    Age=serializers.CharField(max_length=100)
    
    
class Management_Serializer(serializers.Serializer):
    First_Name=serializers.CharField(max_length=100)
    Last_Name=serializers.CharField(max_length=100)
    Mobile=serializers.CharField(max_length=100)
    Email=serializers.CharField(max_length=100)
    Age=serializers.CharField(max_length=100)
       
    
class Library_Serializer(serializers.Serializer):
    Book_Name=serializers.CharField(max_length=100)
    Writer_Name=serializers.CharField(max_length=100)
    Serial_No=serializers.CharField(max_length=100)
    Acquisition_Date=serializers.CharField(max_length=100)
    Return_Date=serializers.CharField(max_length=100)
           
    


