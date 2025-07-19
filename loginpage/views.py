from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout



def loginpage(request):
    if request.method =="POST":
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
             login(request, user)
             return render(request,'index.html')

        else :
             context={
             "error":"your username and password is not match "
        }   
             return render(request,'loginpage.html',context) 









    return render(request,'loginpage.html')



