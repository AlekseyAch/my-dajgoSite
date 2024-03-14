# Generated by Django 5.0.2 on 2024-03-14 14:58

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oneServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directionServices', models.CharField(max_length=250, verbose_name='Направление услуги')),
                ('titleServices', models.CharField(max_length=250, verbose_name='Название услуги')),
                ('imgServices', models.ImageField(upload_to='services_images/', verbose_name='Изображение услуги')),
                ('textServices', ckeditor.fields.RichTextField(verbose_name='Текст услуги')),
                ('videoServices', models.URLField(verbose_name='Ссылка на видео в попап окне')),
                ('imgVideoServices', models.ImageField(upload_to='services_images/', verbose_name='Картинка заглушка видео')),
                ('titleQveschenServices', models.CharField(max_length=250, verbose_name='Заголовок блока вопросы и ответы')),
            ],
        ),
        migrations.CreateModel(
            name='accardionServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleAccardionServicesItem', models.CharField(max_length=250, verbose_name='Заголовок вопроса')),
                ('textAccardionServicesItem', models.TextField(verbose_name='Ответ на вопрос')),
                ('accardionServicesItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Вопрос', to='services.oneservices', verbose_name='Вопросы и ответы')),
            ],
        ),
    ]