from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
# Create your views here.


def home(request):

	return render(request,"student/home.html")


def register(request):
	if request.method=="POST":
		
		name = request.POST["Name"]
		email = request.POST["Mail"]
		phone = request.POST["Phone"]
		age = request.POST["Age"]

		data_db_table = Register(name= name,
								 email= email,
								 phone_num= phone,
								 age= age)
		data_db_table.save()

		data = {"name":name,"mail":email,"phone":phone,"age":age}

		return render(request,"student/data.html",{"data":data})

	return render(request,"student/register.html")