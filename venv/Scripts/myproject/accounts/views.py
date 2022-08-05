from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login (request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request,user)
            return redirect ("/")   
        else :
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')

def register (request):  
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password1= request.POST.get('password1')
        password2= request.POST.get('password2')
        email= request.POST.get('email')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name) 
                user.save()        
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect ('register')
        return redirect ('/')
    else:
        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')

def password_reset(request):
    return render(request, 'password_reset_form.html')