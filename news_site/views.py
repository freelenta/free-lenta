#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.shortcuts import render
from news_site.models import Article
from django.views import generic

class HomeView(generic.ListView):
	template_name = 'news_site/index.html' 
	context_object_name = 'latest_article_list'

	def get_queryset(self):
		return Article.objects.order_by('-pub_date')[:9]

class DetailView(generic.DetailView):
	model = Article
	template_name = 'news_site/detail.html'

def category(request, cat_id):
	articles = Article.objects.filter(category=cat_id)[:9]
	cat_name=''
	if cat_id == 'R':
		cat_name = 'Россия'
	elif cat_id == 'W':
		cat_name = 'Мир'
	elif cat_id == 'U':
		cat_name = 'Бывший СССР'
	elif cat_id	== 'E':
		cat_name = 'Экономика'
	elif cat_id	== 'T':
		cat_name = 'Наука и техника'
	elif cat_id	== 'S':
		cat_name = 'Спорт'
	elif cat_id	== 'C':
		cat_name = 'Культура'
	return render(request, 'news_site/category.html', {'articles':articles, 'cat_name':cat_name})

def about(request):
	return render(request, 'news_site/about.html', {})

def help(request):
	return render(request, 'news_site/help.html', {})