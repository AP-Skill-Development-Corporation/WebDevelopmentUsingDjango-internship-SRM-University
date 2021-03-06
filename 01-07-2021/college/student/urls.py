from django.urls import path
from . import views


urlpatterns = [
	path("register/",views.register),
	path("contact_us/", views.contact_us, name='contact'),
	path("student_register/",views.StudentRegistration, name='register'),
	path("student_data/",views.StudentData,name="all_data"),
	path("<int:Id>/",views.student,name="details"),
	path("update/<int:Id>",views.update,name="update"),
	path("delete/<int:Id>",views.delete,name="delete"),
]