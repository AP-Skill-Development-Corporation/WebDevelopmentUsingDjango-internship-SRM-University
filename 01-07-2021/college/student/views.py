from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
from .forms import ContactForm
from django.core.mail import EmailMessage
from college import settings
from django.contrib import messages
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
		messages.success(req, fname+' Details updated')
		return redirect('all_data')
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
		messages.info(request, data.first_name + ' Details updated Successfully')
		return redirect("all_data")
	return render(request,"student/update.html",{"data":data})

def delete(request,Id):
	data = Register.objects.get(id=Id)
	data.delete()

	return redirect("all_data")


def contact_us(request):
	if request.method == "POST":
		form_data = ContactForm(request.POST)
		if form_data.is_valid():
			form_data.save()
			name = form_data.data['name']
			receiver_mail = form_data.data['mail']
			sub = 'hello from Djnago project'
			sender = settings.EMAIL_HOST_USER
			body = 'hey '+name+", i got the contact us request from you!!!"
			email_msg = EmailMessage(sub, body, sender, [receiver_mail])
			email_msg.send()
			return HttpResponse("Data stored successfully")
		return HttpResponse('getting in-valid data!!')
	empty_form = ContactForm()
	return render(request, "student/contact.html", {'form': empty_form})