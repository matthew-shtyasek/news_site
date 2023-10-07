from django.contrib.auth.models import User
from django.db import models


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
