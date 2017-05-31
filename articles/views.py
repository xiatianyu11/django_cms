# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.

def list(request):
	latest_article_list = Article.objects.order_by('-updateTime')[:5]
	return render(request, 'articles/index.html', {'latest_article_list' : latest_article_list})

def add(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			return render(request, 'success.html')
		else:
			return render(request, 'fail.html')
	else:
		form = ArticleForm()
		return render(request, 'articles/edit.html', {'form' : form})


def edit(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	form = ArticleForm(initial=model_to_dict(article))
	return render(request, 'articles/edit.html', {'form' : form})

def detail(request, article_id):
#	try:
#		article = Article.objects.get(pk=article_id)
#	except Article.DoesNotExist:
#		raise Http404("Article does not exist")
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'articles/detail.html', {'article' : article})
