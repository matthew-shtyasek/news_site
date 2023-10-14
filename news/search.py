from django.contrib.postgres.search import TrigramSimilarity, SearchVector


def news_full_text_search(request, queryset, search_term):
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