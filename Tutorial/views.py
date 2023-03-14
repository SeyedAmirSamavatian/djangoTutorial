from django.http import HttpResponse
from django.shortcuts import render 



def about(request):
	return HttpResponse("salam chetory") 


def contact(request):
	return render(request, 'contact.html')
