from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='Заголовок')
    text = models.TextField(blank=False,
                            verbose_name='Текст')
    publish_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True,
                                     verbose_name='Дата редактирования')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')
    hidden = models.BooleanField(default=False,
                                 blank=False)
    image = models.ImageField(upload_to='%Y/%m/%d',
                              default=f'{settings.STATIC_URL}img/not_found.jpg')
    tags = TaggableManager()

    def __str__(self):
        sliced_title = self.title[:30].rstrip()
        return sliced_title if len(sliced_title) == len(self.title)\
            else sliced_title + '...'
    '''
        Если длина сокращённого заголовка (len(sliced_title)) равна
        длине исходного заголовка (len(self.title)), то мы просто
        возращаем сокращённый заголовок (он будет совпадать с оригинальным,
        поэтому можем вернуть как self.title, так и sliced_title, как
        показано выше).
        В противном случае, когда заголовок всё-таки сократили, 
        мы добавляем к нему многоточие (sliced_title + '...')
    '''

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
