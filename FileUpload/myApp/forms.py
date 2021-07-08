# from django import forms
from django.forms import ModelForm
from .models import profile


class ProfileForm(ModelForm):
	class Meta:
		model = profile
		fields = "__all__"