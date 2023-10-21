from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, PermissionsMixin
from django.forms import Form
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView, CreateView

from news.forms import SearchForm, SortForm, NewsForm
from news.models import News
from news.search import news_full_text_search


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    extra_context = {'form': SearchForm()}

    def get_current_tag(self):
        if self.request.method == 'GET':
            return self.request.GET.get('tag', '')
        return self.request.POST.get('current_tag', '')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['sort_form'] = SortForm(
            initial={'sort_field':
                         self.request.session.get('current_sorting', 'n2o'),
                     'current_tag':
                         self.get_current_tag()})
        return context

    def get_queryset(self):
        sort_fields = {'n2o': '-publish_date',
                       'o2n': 'publish_date',
                       'a-z': 'title',
                       'z-a': '-title'}

        queryset = super().get_queryset()

        tag = self.get_current_tag()

        if tag:
            queryset = queryset.filter(tags__slug=tag)

        if self.request.session.get('is_sort_changed', ''):
            search_term = self.request.session.get('search_term', '')
            self.request.session['is_sort_changed'] = False
        else:
            search_term = self.request.GET.get('search_field', '')
            self.request.session['search_term'] = search_term
        self.request.session.save()

        if search_term:
            queryset, _ = news_full_text_search(self.request,
                                                queryset,
                                                search_term)
        return queryset.order_by(
            sort_fields[self.request.session.get('current_sorting', 'n2o')])

    def post(self, request, *args, **kwargs):
        form = SortForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            request.session['current_sorting'] = cd['sort_field']
            #  self.extra_context['sort_form'] = form
            request.session['is_sort_changed'] = True
            request.session.save()

        return self.get(request, *args, **kwargs)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    permission_required = ['news.add_choice']
    permission_denied_message = 'У вас нет доступа!'

    def form_valid(self, form):
        cd = form.cleaned_data
        news = form.save(commit=False)
        news.author = self.request.user
        news.save()
        news.tags.add(*cd['tags'])
        news.save()
        return redirect(reverse('news:news_list'))

