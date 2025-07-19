from django.shortcuts import render,redirect
from .models import *
from .forms import *
    
def cardioclient(request):
    data = {
        'cardioclients': cardio_client()
    }
    if request.method=="POST":
        client_cardio=cardio_client(request.POST)
        if client_cardio.is_valid():
            client_cardio.save()    


    return render(request,'cardio.html',data)
def cardioclientlist(request):
    data={
        "client": Cardio.objects.all()

    }
    return render(request,"Cardioclientlist.html",data)
def delete(request,id):
    data=Cardio.objects.get(id=id)
    data.delete()
    return redirect("/booking/cardiotablelist/")
