from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    '''  Model for Employee Info '''
    genderchoices = [
        ("Male", "Male"), ("Female", "Female"), ("Others", "Others")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=genderchoices)
    contactno = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} : {self.user.username}"
