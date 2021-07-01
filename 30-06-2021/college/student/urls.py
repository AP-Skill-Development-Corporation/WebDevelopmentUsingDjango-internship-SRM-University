from django.urls import path
from . import views


urlpatterns = [
	path("register/",views.register),
	path("student_register/",views.StudentRegistration),
	path("student_data/",views.StudentData),
]