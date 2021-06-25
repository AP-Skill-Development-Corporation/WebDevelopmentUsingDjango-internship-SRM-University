from django.urls import path
from myApp import views

# from . import views


urlpatterns = [
	path('home/',views.home),
]