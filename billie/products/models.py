from django.db import models

# Create your models here.


class Product(models.Model):
    ''' Product Model for Product Info '''
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    code = models.CharField(max_length=8, unique=True)
    category = models.ManyToManyField('Category')

    def __str__(self) -> str:
        return f"{self.code} : {self.name}"


class Category(models.Model):
    ''' Model for Category Info '''
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return f"{self.code} : {self.name}"
