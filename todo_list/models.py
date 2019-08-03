from django.db import models
import datetime

# Create your models here.

class List(models.Model):
	item=models.CharField(max_length=200,unique=True,blank=True,null=True)
	completed=models.CharField(max_length=50,default="Not Started")
	users=models.CharField(max_length=50,default=None)
	#created=models.DateTimeField(default=None)
	#updated_at=models.DateTimeField(default=None)
	created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at=models.DateTimeField(default=None)


class Data(models.Model):
	username=models.CharField(max_length=200,unique=True)
	password=models.CharField(max_length=20)
	profile=models.ImageField(upload_to='image')