from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Car(models.Model):
    Carname=models.CharField(max_length=50)
    Carimage=models.ImageField(upload_to='image')
    Carmodels=models.IntegerField()
    Owner=models.IntegerField()
    History=models.TextField()
    Contactnumber=models.CharField(max_length=100)
    Location=models.CharField(max_length=50)
    Price=models.IntegerField()
    Kilometer=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
   
    def __str__(self):
        return self.Carname