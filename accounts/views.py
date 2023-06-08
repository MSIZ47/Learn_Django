from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages
from .forms import LoginForm,SignupForm
from .models import CostumUser




def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == 'GET':
        form = LoginForm()
        return render(req, 'registration/login.html',{'form':form})
    elif req.method == 'POST':
            
            form = LoginForm(req.POST)
            password = req.POST.get('password')
            username = req.POST.get('username')
            
            if '@'in username :
                user = CostumUser.objects.get(email=username )
                name = user.username  
                user_email=authenticate(username=name,password=password)
                if user_email is not None:  
                    login(req,user_email)
                    return redirect('/')
                else:
                    messages.add_message(req,messages.ERROR,'Input data is not valid.')
                    return redirect('accounts:login')
            elif '@' not in username:
                user_name=authenticate(username=username,password=password)
                if user_name is not None:  
                    login(req,user_name)
                    return redirect('/')
                else:
                    messages.add_message(req,messages.ERROR,'Input data is not valid.')
                    return redirect('accounts:login')
            else:
                messages.add_message(req,messages.ERROR,'Input data is not valid.')
                return redirect('accounts:login')
    # else:
    #     messages.add_message(req,messages.ERROR,'Input data is not valid.')
    #     return redirect('accounts:login')


@login_required
def Logout(req):
     logout(req)
     return redirect('/')
     

def signup(req):
    if req.method == 'GET':
        form = SignupForm()
        return render(req, 'registration/signup.html' , {'form':form})
    elif req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            username = req.POST.get('username')
            password = req.POST.get('password1')
            email = req.POST.get('email')
            image = req.POST.get('image')
            id_code = req.POST.get('id_code')
            user=authenticate(username=username,password=password,email=email,image=image,id_code=id_code)
            if user is not None:  
                login(req,user)
                return redirect('/')
        else:
            messages.add_message(req,messages.ERROR,'Input data is not valid.')
            return redirect('accounts:login')
        

    