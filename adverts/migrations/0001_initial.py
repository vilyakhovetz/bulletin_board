# Generated by Django 4.1.4 on 2023-01-03 01:08

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('publication_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('edit_datetime', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('building_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер строения')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-edit_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='adverts.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CategoryCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('category', models.ManyToManyField(related_name='characteristics', to='adverts.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Характеристика категории',
                'verbose_name_plural': 'Характеристики категорий',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advert_photos/%Y/%m/%d', verbose_name='Фото к объявлению')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='adverts.advert', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Фото к объявлению',
                'verbose_name_plural': 'Фото к объявлению',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='adverts.advert', verbose_name='Объявление')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='adverts.categorycharacteristic', verbose_name='Характеристика')),
            ],
            options={
                'verbose_name': 'Значение характеристики',
                'verbose_name_plural': 'Значения характеристик ',
            },
        ),
    ]
