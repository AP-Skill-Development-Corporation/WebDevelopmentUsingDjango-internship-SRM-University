from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def signup(request):
	form = UserReg(request.POST or None)
	if form.is_valid():
		form.save()
		user = User.objects.last()
		login(request,user)
		return redirect("profile_details",user.id)

	return render(request,"signup.html",{"form":form})


def signin(request):
	if request.method=="POST":
		uname = request.POST["uname"]
		password = request.POST["pswd"]

		user = authenticate(username=uname,password=password)
		if user:
			login(request,user)
			return redirect("home")
		else:
			messages.info(request,"Invalid username of password")
			return redirect("signup")

	return render(request,"login.html")


def signout(request):
	logout(request)
	return redirect("home")


def profile_details(request, Id):
	if request.method=="POST":
		user = User.objects.get(id=Id)
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.user_id = user.id
			f.save()
			return redirect("profile",Id)
	form = ProfileForm()
	return render(request,"profile_details.html",{"form":form})


def profile(request, Id):
	u = User.objects.get(id=Id)
	p = profileDetails.objects.get(user_id=Id)
	return render(request,"profile.html",{"u":u,"p":p})


def update(request,Id):
	u = User.objects.get(id=Id)
	p = profileDetails.objects.get(user_id = Id)
	if request.method=="POST":
		form = ProfileForm(request.POST,request.FILES, instance=p)
		if form.is_valid():
			form.save()
		return redirect("profile",Id)
	form = ProfileForm(instance=p)
	return render(request,"update.html",{"p":form})

