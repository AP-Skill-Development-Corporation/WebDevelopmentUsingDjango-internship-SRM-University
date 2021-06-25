from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
	return HttpResponse("Welcome to Django")


def sample(request):

	return HttpResponse("<h1>This is my Sample Page</h1><br><p>This is my first project in django</p>")

def projectHome(request):
	message = "<h3>This is my Project Home page</h3>"
	return HttpResponse(message)

def name(request,Django):
	return HttpResponse(Django)


def roll(request, roll):
	message = "Roll Number is " + str(roll)
	return HttpResponse(message)

def table(request,number):
	table = ""
	for i in range(1,11):
		line = "{} x {} = {}".format(number,i,number*i)


	return HttpResponse(line)


