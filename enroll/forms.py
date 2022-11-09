from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class StudentForm(UserCreationForm):
	designation = forms.CharField(max_length = 40)
	class Meta:
 		model = User 
 		fields = ['username','first_name', 'last_name', 'email']
 		labels = {'email': 'Email'}
        

class EditForm(UserChangeForm):
	password = None
	designation = forms.CharField(max_length = 40)
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'date_joined', 'designation']
		labels = {'email': 'Email'}
