from django.shortcuts import render
from .models import Article
# Create your views here.
from .forms import Send_Article

def footer(request):
# ........................................................ baraye form ersal article
	if request.method == "POST":
		form = Send_Article(request.POST)
		if form.is_valid():
			title = form.cleaned_data['Title']
			body = form.cleaned_data['Body']
			# date = form.cleaned_data['Date']
			article = Article.objects.create(title=title, body=body)
			article.save()
			form = Send_Article()
	else:
		form = Send_Article()
# ......................................................... baraye form ersal article

	articles = Article.objects.all().order_by('date')
	return render(request,'footer.html', {'articles':articles, 'form':form})

#######################################################################################################


def footer_detile(request,id):
	articles = Article.objects.get(id = id)
	return render(request,'article_detile.html', {'articles':articles})