from django import forms
from django.forms import ModelForm, Form

from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')