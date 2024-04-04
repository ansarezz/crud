# Generated by Django 4.1.13 on 2024-04-04 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='is_realted_price',
        ),
        migrations.AddField(
            model_name='board',
            name='is_related_price',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='board',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 4, 16, 27, 41, 871221), verbose_name='Дата и время публикации'),
        ),
    ]
