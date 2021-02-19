from django.db import models
from django.contrib import admin
# Create your models here.
class Order(models.Model):
  username = models.CharField(max_length=15,blank=True)
  email = models.EmailField(max_length=70,blank=True)
  password1 = models.CharField(max_length=50,blank=True)
  password2 = models.CharField(max_length=50,blank=True)


class Forminfo(models.Model):
 name = models.CharField(max_length=50)
 email = models.EmailField(max_length=50)
 telephone = models.IntegerField()
 subjectname = models.CharField(max_length=50)
 description = models.CharField(max_length=50)
 docfile = models.FileField(upload_to='documents/%Y/%m/%d')

 def __str__(self):
  return self.name

