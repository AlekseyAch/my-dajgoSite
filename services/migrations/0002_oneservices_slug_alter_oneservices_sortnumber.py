# Generated by Django 5.0.2 on 2024-03-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oneservices',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='oneservices',
            name='sortNumber',
            field=models.IntegerField(default=1, verbose_name='Поле сортировки'),
        ),
    ]
