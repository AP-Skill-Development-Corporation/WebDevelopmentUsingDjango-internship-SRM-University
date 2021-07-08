from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profileDetails(models.Model):
	branches = (
		("CSE","cse"),
		("ECE","ece"),
		("IT","it"),
		("CE","ce"),
		("MECH","mech")
		)
	branch = models.CharField(max_length=10,choices = branches)
	phone = models.CharField(max_length=10)
	roll = models.CharField(max_length=20)
	image = models.ImageField(upload_to="users/",default="default.png")
	user = models.OneToOneField(User,on_delete = models.CASCADE)


	def __str__(self):
		return self.user.first_name