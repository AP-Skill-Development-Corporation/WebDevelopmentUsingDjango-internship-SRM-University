from django.shortcuts import render, redirect
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

def StudentRegistration(req):
	if req.method=="POST":
		fname = req.POST["fname"]
		lname = req.POST["lname"]
		email = req.POST["mail"]
		ph = req.POST["phno"]
		age = req.POST["age"]

		student = Register(first_name=fname,last_name=lname,email=email,phone_num=ph,age=age)
		student.save()

		return HttpResponse("Registration Successful")


	return render(req,"student/student_register.html")

def StudentData(request):
	
	data = Register.objects.all()
	return render(request,"student/student_data.html",{"data":data})


def student(request, Id):
	data = Register.objects.get(id=Id)
	return render(request,"student/details.html",{"data":data})

def update(request, Id):
	data = Register.objects.get(id=Id)
	if request.method=="POST":
		data.first_name = request.POST["fname"]
		data.last_name = request.POST["lname"]
		data.email = request.POST["mail"]
		data.phone_num = request.POST["phno"]
		data.age = request.POST["age"]

		data.save()
		return redirect("details",Id)
	return render(request,"student/update.html",{"data":data})

def delete(request,Id):
	data = Register.objects.get(id=Id)
	data.delete()

	return redirect("all_data")


