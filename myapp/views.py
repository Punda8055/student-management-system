from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from . models import User
# Create your views here.
#This function  will add  new items and  show all items
def add_show(request):
    if request.method=="POST":
        fm=Student(request.POST)
        if fm.is_valid():
            sname=fm.cleaned_data['name']
            semail=fm.cleaned_data['email']
            spass=fm.cleaned_data['password']
            reg=User(name=sname,email=semail,password=spass) #craete object
            reg.save()
            fm=Student() # after add student form become blank

         
    else:
        fm=Student()
    stud=User.objects.all() #empty on non empty it data showing
    return render(request,'myapp/addshow.html',{'form':fm,'stu':stud})
#This function  delete items
def delete_data(request,id):
    if request.method=='POST': # secure this method also directly use get
        pi=User.objects.get(pk=id) # primary key
        pi.delete()
        return HttpResponseRedirect('/')

#This function  Update items
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Student(request.POST,instance=pi) #instance -instance variable
        if fm.is_valid():
         fm.save()
         return HttpResponseRedirect('/')
    else:
       pi=User.objects.get(pk=id)
       fm=Student(instance=pi)
    return render(request,'myapp/updatestudent.html',{'form':fm})