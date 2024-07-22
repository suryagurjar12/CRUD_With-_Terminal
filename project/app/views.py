from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
     # data=Student.objects.all()                            #totel data show krane ke liye 
     # data=Student.objects.filter(stu_city='bhopal')        #jo name ya city chahiye usko filter krne ke liye 
     # data=Student.objects.order_by('stu_name')             # oder form m dene ke liye 
     # data=Student.objects.order_by('-stu_name')            # unoder  form m dene ke liye 
     # data=Student.objects.order_by().first()               #first value dekhne ke liye 
     # data=Student.objects.order_by().last()                #last value dekhne ke liye 
     # data=Student.objects.order_by().reverse()             #revers order mai value dekhne ke liye
     # data=Student.objects.exclude(stu_name='surya').exclude(stu_city='bhopal')  #ye name dobara repied na ho or city ke liye  
     # data=Student.objects.order_by("?")                       #ye sir se puchna hai
     # data=Student.objects.values('stu_name',"stu_city")       #jo value dekhna hai uske liye
     # data=Student.objects.order_by('stu_name')[0:3]           #sliceing mathod 2 
     # data=Student.objects.all()[::-1][:5]                     #reverse sliceing
     data=Student.objects.values('stu_name',"stu_city")[::-1][:2]
     
      
    
     print(data)
     # print(data.values())
     
     return HttpResponse("<h1>welcome to home page</h1>")



#py manage.py shell                ---> shell terminal open 
# from app.models import Student   ---> jo bhi class bnai hai import krna hota hai 
# Student.objects.all()            ---> models.objects.all() --> data query mail show krne ke liye 

#---------------Create----------------------

#stu1=student(stu_name="surya Gurjar",stu_city="bhopal",stu_email="surya@gamil.com") --->stu1 name ka ek veriable lena hota hai or details fill krna hota hai
#stu1.save()    ---> save krna pdega tabhi data show hoga 


#multipal data tables bnane ke liye
#stu2=student(stu_name="Ram Gurjar",stu_city="indore",stu_email="ram@gamil.com") 
#stu3=student(stu_name="Narayan Gurjar",stu_city="dehli",stu_email="narayan@gamil.com") 
#stu4=student(stu_name="Amit Gurjar",stu_city="mumbai",stu_email="amit@gamil.com") 
#stu5=student(stu_name="Raghav Gurjar",stu_city="pune",stu_email="raghav@gamil.com") 

#stu=[stu1,stu2,stu3,stu4,stu5]
#for i in stu:
#     i.save()


#---------------Read---------------
#Student.objects.all()      --->show all data 

#x=Student.objects.all() 
#x

#x=Student.objects.all().count(1)  --->count mathod (0,1,2,3,4,5,)
#x

#x=Student.objects.all()[1]     ---> indexing  check 
#x


#x=Student.objects.all()[0:4]    --->sliceing krne ke liye
#x

#x=Student.objects.all()[::-1][:2]   --->reverse sliceing
#x

#x=Student.objects.all().first()     --->first value check krne ke liye 
#                       .last()
#                       .reverse()
#x


#-------------------Update------------------

#x=Student.objects.all(1)   --> id dena pdta hai jisko rename ya update krne ke liye 
#x

#x.stu_name
#x

#x.stu_name="suryakant"
#x.save()

#x.stu_email="gurja@gamil.com"
#x.save()

#x.stu_city="Gadarwara"
#x.save()


#----------------delete------------

#x=Student.objects.all(1) 
#x

#x.delete
#(1{'app.Student':1})
#x
#x.save()
