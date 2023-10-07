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
                    'hidden',
                    'tag_list']
    list_filter = ['publish_date',
                   'edit_date',
                   'hidden',
                   'tags']
    search_fields = ['title']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    '''Получаем данные из связанной таблицы одним запросом
    queryset - ленивый объект, он не отправит запрос в БД до тех пор,
    пока мы не запросим конкретные данные. А значит мы можем продолжать с
    ним работать без потерь в производительности (это мы использовали
    в поиске и здесь, когда написали "prefetch_related", который
    позволяет получить одним запросом данные из таблицы news и объединить
    их с данными из связанной таблицы tags'''

    def tag_list(self, obj):
        return ', '.join(news.name for news in obj.tags.all())

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

