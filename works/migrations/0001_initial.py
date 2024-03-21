# Generated by Django 5.0.3 on 2024-03-17 15:35

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorksCategoryItem', models.CharField(max_length=500, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=250, verbose_name='Ссылка')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='works.workscategory', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категория проектов',
                'verbose_name_plural': 'Категории проектов',
            },
        ),
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleWorks', models.CharField(max_length=250, verbose_name='Название услуги')),
                ('slug', models.SlugField(blank=True, help_text='Заполняется автоматически', max_length=250, verbose_name='Ссылка')),
                ('imgWorks', models.ImageField(upload_to='works/', verbose_name='Главное изображение')),
                ('clientWorks', models.CharField(max_length=500, verbose_name='Клиент/Компания')),
                ('dateWorks', models.DateField(verbose_name='Дата старта проекта')),
                ('dateWorksTy', models.DateField(verbose_name='Дата завершения проекта')),
                ('linkWorks', models.URLField(verbose_name='Ссылка на проект')),
                ('textWorks', ckeditor.fields.RichTextField(verbose_name='Первое описание проекта')),
                ('stepsWorks', ckeditor.fields.RichTextField(verbose_name='Текст после заголовока что было сделано')),
                ('resultWorks', ckeditor.fields.RichTextField(verbose_name='Текст после заголовока результаты проекта')),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.workscategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='WorksGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgWorksGallery', models.ImageField(upload_to='works/', verbose_name='Главное изображение')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='works.works', verbose_name='Галерея проекта')),
            ],
            options={
                'verbose_name': 'Галерея проекта',
                'verbose_name_plural': 'Галерея проекта',
            },
        ),
    ]
