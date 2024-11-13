# Generated by Django 5.1.1 on 2024-11-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True 

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=200, verbose_name='Заголовок новости')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('status', models.CharField(choices=[('draft', 'На модерации'), ('publish', 'Готово к публикации'), ('inactive', 'Неактивное')], default='draft', max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]