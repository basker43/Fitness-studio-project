from django.shortcuts import render,redirect
from .models import *
from .forms import *

def strenghtclient(request):
    data = {
        'strengthclients': Strength_client()
    }
    if request.method=="POST":
        client_strength=Strength_client(request.POST)
        if client_strength.is_valid():
            client_strength.save()    


    return render(request,'strenghtclient.html',data)
def strengthtable(request):
    data={
        'strengthtable':Strength.objects.all()

    }
    return render (request,'strengthtable.html',data)


def delete(request,id):
    data=Strength.objects.get(id=id)
    data.delete()
    return redirect("/strength/strengthbooking/")
