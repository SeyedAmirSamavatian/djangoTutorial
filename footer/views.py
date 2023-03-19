from django.shortcuts import render
from .models import Article
# Create your views here.

def footer(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'footer.html', {'articles':articles})



def footer_detile(request,id):
	articles = Article.objects.get(id = id)
	return render(request,'article_detile.html', {'articles':articles})