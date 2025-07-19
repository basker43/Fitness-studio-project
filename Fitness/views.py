from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'home.html')  
def fitnesspage(request):
    
    return render(request,'Fitnessclass.html')
def yogaclient(request):
    data = {
        'yogaclients': yoga_client()
    }
    if request.method=="POST":
        client_yoga=yoga_client(request.POST)
        if client_yoga.is_valid():
            client_yoga.save()    


    return render(request,'yogaclient.html',data)
def yogaclientlist(request):
    data={
        "client": Yoga.objects.all()

    }
    return render(request,"yogaclientlist.html",data)
def delete(request,id):
    data=Yoga.objects.get(id=id)
    data.delete()
    return redirect("/home/yogaclientlist/")


