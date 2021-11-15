from django.db import models

# Create your models here.
class newsletter1(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=20)
