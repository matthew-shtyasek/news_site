from django.forms import Form
from django.shortcuts import render
from django.views.generic import ListView, FormView

from news.forms import SearchForm, SortForm
from news.models import News
from news.search import news_full_text_search


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    extra_context = {'form': SearchForm(),
                     'sort_form': SortForm()}
    current_sorting = 'n2o'

    def get_queryset(self):
        sort_fields = {'n2o': '-publish_date',
                       'o2n': 'publish_date',
                       'a-z': 'title',
                       'z-a': '-title'}

        queryset = super().get_queryset()
        search_term = self.request.GET.get('search_field', '')
        if search_term:
            queryset, _ = news_full_text_search(self.request,
                                                queryset,
                                                search_term)
        return queryset.order_by(sort_fields[self.current_sorting])

    def post(self, request, *args, **kwargs):
        form = SortForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            self.current_sorting = cd['sort_field']
            self.extra_context['sort_form'] = form

        return self.get(request, *args, **kwargs)
