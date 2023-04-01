from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
# from django.contrib.auth.models import User

from .forms import RegisterUserForm

def registery(request):
	if request.method=="POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			# email = form.cleaned_data['email']
			# user_email_count = User.objects.filter(email=email).count()
			# if user_email_count > 0:
			# user = authenticate(username=username, password=password, email=email)
			
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Registration Successful!'))
			return redirect('footer')
	else:
		form = RegisterUserForm()

	return render(request, 'register.html',{'form':form})	

