# Generated by Django 4.2.5 on 2023-10-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-publish_date', '-edit_date'), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
    ]
