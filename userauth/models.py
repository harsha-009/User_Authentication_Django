from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

		db_table='users'

class users(models.Model):
	username=models.CharField(max_length=40)
	password=models.CharField(max_length=20)

