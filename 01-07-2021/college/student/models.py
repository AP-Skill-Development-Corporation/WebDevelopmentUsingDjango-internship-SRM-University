from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=30,default="")
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length = 10)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.first_name

class ContactUs(models.Model):
    name = models.CharField(max_length=10)
    mail = models.EmailField()
    Gender_choices = (('Male','male'),
                      ('Female','female'))
    gender = models.CharField(max_length=6, choices=Gender_choices,
                              blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name