# Generated by Django 4.2.5 on 2023-10-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_options_news_image_news_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='/media/defaults/not_found.jpg', upload_to='%Y/%m/%d'),
        ),
    ]
