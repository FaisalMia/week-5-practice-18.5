from django.shortcuts import render,redirect
from .forms import SignupForm
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # return redirect('home')
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
     signup_form =SignupForm(request.POST)
     if signup_form.is_valid():
         messages.success(request,"Account Created Successfully!")
         signup_form.save()
         return redirect('signup')
    else:
        signup_form = forms.SignupForm()
    return render(request,'signup.html',{'form' : signup_form , 'type' : 'SignUp'})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                
                user = authenticate(username=name,password=user_pass)
                if user is not None:
                    messages.success(request,'Logged in Successfully!')
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.warning(request,'Login information is incorrect!')
                    return redirect('signup')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form' : form})
    else:
        return redirect('profile')
    
def user_logout(request):
    messages.success(request,'Logged Out Successfully!')
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user' : request.user})
    else:
        return redirect('user_login')
    
def passchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated Successfully!')
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form' : form})
    else:
        return redirect('user_login')
    
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated Successfully!')
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form' : form})
    else:
        return redirect('user_login')
    
            