from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import profile

from django.http import HttpResponse



def user(request):
	form = ProfileForm()
	if request.method=="POST":
		form = ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			# return HttpResponse("<h1>Successfully uploaded</h1>")
			return redirect("data")
	return render(request,"profile.html",{"form":form})



def data(request):
	d = profile.objects.all()
	return render(request,"data.html",{"d":d})