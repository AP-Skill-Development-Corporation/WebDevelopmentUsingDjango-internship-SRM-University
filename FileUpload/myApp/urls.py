from django.urls import path

from . import views


urlpatterns = [
	path("profile/",views.user,name="profile"),
	path("data/",views.data,name="data"),
]
