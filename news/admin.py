from django.contrib import admin
from django.contrib.postgres.search import SearchVector, TrigramSimilarity

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = []
    readonly_fields = ['publish_date',
                       'edit_date']
    list_display = ['title',
                    'publish_date',
                    'edit_date',
                    'author',
                    'hidden']
    search_fields = ['title',
                     'text',
                     'author__username',
                     'author__first_name',
                     'author__last_name']
    list_filter = ['publish_date',
                   'edit_date',
                   'hidden']

    def get_search_results(self, request, queryset, search_term: str):
        if not search_term.strip():
            return queryset, False

        title_queryset = queryset.annotate(
            similarity=TrigramSimilarity('title', search_term)
        ).filter(similarity__gt=0.03).order_by('-similarity')

        authors_queryset = queryset.annotate(
            similarity=TrigramSimilarity('author__username', search_term)
        ).filter(similarity__gt=0.3).order_by('-similarity')

        text_search_vector = SearchVector('text')
        text_queryset = queryset.annotate(
            search=text_search_vector
        ).filter(search=search_term)

        result_queryset = title_queryset | authors_queryset | text_queryset
        result_queryset = result_queryset.distinct()

        return result_queryset, False

