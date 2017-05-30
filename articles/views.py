# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.

def list(request):
	latest_article_list = Article.objects.order_by('-updateTime')[:5]
	return render(request, 'articles/index.html', {'latest_article_list' : latest_article_list})

def add(request):
	return render(request, 'articles/add.html')

def edit(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		data = model_to_dict(article)
		form = ArticleForm(initial=data)
		form.as_p()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'articles/edit.html', {'form' : form})

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'articles/detail.html', {'article' : article})
