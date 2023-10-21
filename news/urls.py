from django.urls import path
from django.views.generic import DetailView

from news.models import News
from news.views import NewsListView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/',
         DetailView.as_view(model=News,
                            template_name='news/news_details.html',
                            context_object_name='news'),
         name='details')
]
