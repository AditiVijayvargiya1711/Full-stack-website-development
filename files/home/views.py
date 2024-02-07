from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from home.models import Profile
from home.models import Uploading
# Create your views here.
def home(request):
    if request.user.is_authenticated==True:
        return render(request,"home.html")
    else:
        return render(request,"signin_login.html")
def signinsite(request):
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            if username=="" or password=="":
                return render(request,"signin_login.html")
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                login(request,user)
                return render(request,"profile1.html")
def loginsite(request):
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(username=username,password=password)
            if user is None:
                return render(request,"signin_login.html")
            else:
                login(request,user)
                return render(request,"home.html")
def signin_login(request):
        if request.user.is_authenticated==True:
            logout(request)
            return render(request,"signin_login.html")
        else:
            return render(request,"signin_login.html")
def profile2(request):
        if request.user.is_authenticated==True:
            user=Profile.objects.get(username=request.user.username)
            dict={
                "name":user.name,
                "bio":user.bio,
                "location":user.location,
                "socialaccount1":user.socialaccount1,
                "socialaccount2":user.socialaccount2,
                "socialaccount3":user.socialaccount3
            }
            return render(request,"profile2.html",dict)
        else:
            return render(request,"signin_login.html")
def profile1(request):
    if request.user.is_authenticated==True:
        return render(request,"profile1.html")
    else:
        return render(request,"signin_login.html")
def saveprofile(request):
    if request.user.is_authenticated==True:
        if request.method=="POST":
            username=request.user.username
            name=request.POST.get("name")
            bio=request.POST.get("bio")
            location=request.POST.get("location")
            socialaccount1=request.POST.get("socialaccount1")
            socialaccount2=request.POST.get("socialaccount2")
            socialaccount3=request.POST.get("socialaccount3")
            profile=Profile(username=username,name=name,bio=bio,location=location,socialaccount1=socialaccount1,socialaccount2=socialaccount2,socialaccount3=socialaccount3)
            profile.save()
            return render(request,"home.html")
def upload(request):
    if request.user.is_authenticated==True:
        return render(request,"upload.html")
    else:
        return render(request,"signin_login.html")
def profile3(request):
    if request.user.is_authenticated==True:
        return render(request,"update.html")
    else:
        return render(request,"signin_login.html")
def updateprofile(request):
    if request.user.is_authenticated==True:
        if request.method=="POST":
            user=Profile.objects.get(username=request.user.username)
            user.name=request.POST.get("name")
            user.bio=request.POST.get("bio")
            user.location=request.POST.get("location")
            user.socialaccount1=request.POST.get("socialaccount1")
            user.socialaccount2=request.POST.get("socialaccount2")
            user.socialaccount3=request.POST.get("socialaccount3")
            user.save()
            dict={
                "name":user.name,
                "bio":user.bio,
                "location":user.location,
                "socialaccount1":user.socialaccount1,
                "socialaccount2":user.socialaccount2,
                "socialaccount3":user.socialaccount3
            }
            return render(request,"profile2.html",dict)
    else:
        return render(request,"signin_login.html")
def upload1(request):
    if request.user.is_authenticated==True:
        if request.method=="POST" and request.FILES["file"]:
            username=request.user.username
            file=request.FILES["file"]
            uploading=Uploading(username=username,file=file)
            uploading.save()
            return render(request,"upload.html")
    else:
        return render(request,"signin_login.html")
#admin
#admin