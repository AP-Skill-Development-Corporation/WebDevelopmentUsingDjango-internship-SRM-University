from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def signup(request):
	form = UserReg(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("home")

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
