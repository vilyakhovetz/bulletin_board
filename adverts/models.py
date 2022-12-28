from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, primary_key=True, verbose_name='Название')
    slug = models.SlugField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.parent.name} -> {self.name}' if self.parent else self.name


class Advert(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    content = models.TextField(verbose_name='Содержание')
    price = models.IntegerField(verbose_name='Цена')
    publication_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    address = models.CharField(max_length=200, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-edit_datetime']

    def __str__(self):
        return self.title


class Photo(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='photos', verbose_name='Объявление')
    image = models.ImageField(upload_to='advert_photo/%Y/%m/%d', verbose_name='Фото к объявлению')

    class Meta:
        verbose_name = 'Фото к объявлению'
        verbose_name_plural = 'Фото к объявлению'


class CategoryCharacteristic(models.Model):
    category = models.ManyToManyField(Category, related_name='characteristics', verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика категории'
        verbose_name_plural = 'Характеристики категорий'


class CharacteristicValue(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='values', verbose_name='Объявление')
    characteristic = models.ForeignKey(CategoryCharacteristic, on_delete=models.CASCADE, related_name='values',
                                       verbose_name='Характеристика')
    value = models.CharField(max_length=50, verbose_name='Значение')

    class Meta:
        verbose_name = 'Значение характеристики'
        verbose_name_plural = 'Значения характеристик '

    def __str__(self):
        return f'{self.characteristic.name}: {self.value}'