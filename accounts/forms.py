from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=70)
	last_name = forms.CharField(max_length=70)
	class Meta:
		model = User 
		fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2' )
		# user_email_count = User.objects.filter(email=email).count()
		# if user_email_count > 0: