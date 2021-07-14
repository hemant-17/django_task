from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserProfileSerializer

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
                userprofile_obj=UserProfile(user=user,email=email)
                userprofile_obj.save()
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

@login_required(login_url='/login')
def index(request):
    #Fetching the info of the user and updating it
    data=(UserProfile.objects.filter(user=request.user.id).values_list('name','email','dob','mobile_no'))[0]
    name=data[0]
    email=data[1]
    dob=data[2]
    mobile_no=data[3]
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile_number=request.POST['phone_no']
        userprofile_obj=UserProfile.objects.filter(user=request.user.id).update(name=name,email=email,mobile_no=mobile_number)
        data=(UserProfile.objects.filter(user=request.user.id).values_list('name','email','dob','mobile_no'))[0]
        name=data[0]
        email=data[1]
        dob=data[2]
        mobile_no=data[3]
        messages.info(request, 'Information Updated')
        return render(request,'index.html',{'name':name,'email':email,'dob':dob,'mobile_no':mobile_no})

    return render(request,'index.html',{'name':name,'email':email,'dob':dob,'mobile_no':mobile_no})

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')

##Rest Framework views
class UserProfileList(APIView):
    def get(self,request):
        userprofile=UserProfile.objects.all()
        serializer=UserProfileSerializer(userprofile,many=True)
        return Response(serializer.data)

#Get Profile info
@api_view(['GET'])
def api_profile_view(request,id):
    try:
        profile=UserProfile.objects.get(user=id)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer=UserProfileSerializer(profile)
        return Response(serializer.data)

#Update profile info
@api_view(['PUT'])
def api_profile_update(request,id):
    try:
        profile=UserProfile.objects.get(user=id)
        print(profile)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='PUT':
        print(request.data)
        serializer=UserProfileSerializer(profile,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#Delete Profile Info
@api_view(['DELETE'])
def api_profile_delete(request,id):
    try:
        profile=UserProfile.objects.get(user=id)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='DELETE':
        operation=profile.delete()
        data={}
        if operation:
            data["success"]="delete successful"
        else:
            data["failure"]="delete failed"
        return Response(data=data)

#Create Profile
@api_view(['POST'])
def api_profile_add(request,id):
    user=User.objects.get(pk=id)
    profile=UserProfile(user=user)
    if request.method=='POST':
        print(request.data)
        serializer=serializer=UserProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)