from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class UserReg(UserCreationForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","username","email"]



class ProfileForm(ModelForm):
	class Meta:
		model = profileDetails
		fields = ["branch","phone","roll"]