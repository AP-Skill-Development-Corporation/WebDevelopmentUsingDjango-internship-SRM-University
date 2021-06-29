from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_num = models.CharField(max_length = 20)
    age = models.IntegerField()

    def __str__(self):
        return self.name +' '+ self.email + self.phone_num