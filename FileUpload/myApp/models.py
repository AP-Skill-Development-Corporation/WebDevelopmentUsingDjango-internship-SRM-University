from django.db import models

# Create your models here.


class profile(models.Model):
	name = models.CharField(max_length=20)
	image = models.ImageField(upload_to="users/")


	def __str__(self):
		return self.name