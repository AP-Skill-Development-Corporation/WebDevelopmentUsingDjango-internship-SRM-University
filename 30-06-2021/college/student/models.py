from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=30,default="")
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length = 10)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.first_name