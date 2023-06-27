from django.shortcuts import render,redirect

from .models import Donar_Model,Agent_Model,Assign_Model

from .forms import Donar_ModelCreate,Agent_ModelCreate,Assign_ModelCreate

import sys
# Create your views here.

def index(request):

    return render(request,'index.html')


def about(request):

    return render(request,'about.html')

def donate(request):

    upload=Donar_ModelCreate()

    if request.method=='POST':
        
        upload=Donar_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('donatesuccess')
        
    else:
        
        return render(request,'donate.html',{'upload_form':upload})


def admin1(request):

    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            if(username=="admin" and password=="admin"):
                
                request.session["name"]=username

                return redirect('AdminHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


    return render(request,'admin.html')

def contact(request):

    return render(request,'contact.html')

def agent(request):

    if request.method == "POST":
        
        name=request.POST.get('username')
        password=request.POST.get('password')

        try:
            print("Hello world",name,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=Agent_Model.objects.get(name=name,password=password)

            print(enter.id)
            request.session["id"]=enter.id 
            request.session["name"]=enter.name
           


            return redirect('AgentHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    return render(request,'agent.html')

def donatesuccess(request):

    return render(request,'donatesuccess.html')

def AdminHome(request):
    return render(request,'AdminHome.html')


def AgentHome(request):

    name=request.session['name']

    return render(request,'AgentHome.html',{'name':name})


def AddAgent(request):

    upload=Agent_ModelCreate()

    if request.method=='POST':
        
        upload=Agent_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('AddAgent')
        
    else:
        
        return render(request,'AddAgent.html',{'upload_form':upload})


    
def ViewAgent(request):

    obj=Agent_Model.objects.all()

    return render(request,'ViewAgents.html',{'obj':obj})



def update_agent(request,a_id):
    a_id=int(a_id)

    print("The aid is ",a_id)

    try:
        a_sel=Agent_Model.objects.get(id=a_id)
    
    except Agent_Model.DoesNotExist:
        return redirect('index')

    f_form=Agent_ModelCreate(request.POST or None, instance=a_sel)

    if f_form.is_valid():

        f_form.save()

        return redirect('ViewAgent')
    
    return render(request,'AddAgent.html',{'upload_form':f_form})



def delete_agent(request,a_id):

    a_id=int(a_id)
    try:

        a_sel=Agent_Model.objects.get(id=a_id)

    except Agent_Model.DoesNotExist:
        pass

    a_sel.delete()
    return redirect('ViewAgent')

def ViewSDonars(request,c_id):

    c_id=int(c_id)

    obj=Donar_Model.objects.all().filter(id=c_id)

    
    return render(request,'ViewSDonars.html',{'obj':obj})



def ViewDonars(request):

    obj=Donar_Model.objects.all()

    return render(request,'ViewDonars.html',{'obj':obj})

def ViewADonars(request):

    id=request.session['id']

    obj=Assign_Model.objects.all().filter(aid=id)

    
    return render(request,'ViewADonars.html',{'obj':obj})

def AssignDonars(request):

    upload=Assign_ModelCreate()

    try:

            if request.method=='POST':
        
                 upload=Assign_ModelCreate(request.POST,request.FILES)

                 if upload.is_valid():

                    upload.save()

                    return redirect('AssignDonars')
                 else:
                    return redirect('AssignDonars')
        
            else:
        
                 return render(request,'AssignDonars.html',{'upload_form':upload})
    except:

            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


def ViewAssignAgents(request):

    obj=Assign_Model.objects.all()

    return render(request,'ViewAssignAgents.html',{'obj':obj})







