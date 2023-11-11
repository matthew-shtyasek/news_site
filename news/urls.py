from django.urls import path
from django.views.generic import DetailView, CreateView

from news.api_views import NewsDetailApiView, NewsListApiView
from news.forms import NewsForm
from news.models import News
from news.views import NewsListView, NewsCreateView, NewsEditView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/',
         DetailView.as_view(model=News,
                            template_name='news/news_details.html',
                            context_object_name='news'),
         name='details'),
    path('create/', NewsCreateView.as_view()),
    path('edit/<int:pk>/', NewsEditView.as_view(), name='edit'),

    path('api-news/<int:id>/', NewsDetailApiView.as_view()),
    path('api-news-list/', NewsListApiView.as_view())
]
