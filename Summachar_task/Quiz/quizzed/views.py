from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# from .models import UserProfile
from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from . serializers import UserProfileSerializer

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1= request.POST.get('password1','')
        password2= request.POST.get('password2','')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered ')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1 )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Confirm password did not match ')
            return redirect('register')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,User)
            request.session['username'] = username
            return redirect("index")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')


def index(request):
    return render(request,'index.html')

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')
