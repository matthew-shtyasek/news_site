from django.contrib import admin

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
                     'author']
    list_filter = ['publish_date',
                   'edit_date',
                   'hidden']
