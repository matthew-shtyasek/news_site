from django.urls import path
from django.views.generic import DetailView, CreateView

from news.forms import NewsForm
from news.models import News
from news.views import NewsListView, NewsCreateView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/',
         DetailView.as_view(model=News,
                            template_name='news/news_details.html',
                            context_object_name='news'),
         name='details'),
    path('create/', NewsCreateView.as_view())
]
