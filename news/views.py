from django.shortcuts import render
from django.views.generic import ListView

from news.models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
