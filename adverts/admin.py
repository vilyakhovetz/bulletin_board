from django.contrib import admin
from adverts.models import *


class PhotoInline(admin.TabularInline):
    model = Photo


class CharacteristicValueInline(admin.TabularInline):
    model = CharacteristicValue


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author')
    list_display_links = ('title',)
    inlines = [PhotoInline, CharacteristicValueInline]
    search_fields = ('title', 'author__email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)


class CategoryCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories')
    list_display_links = ('name',)
    search_fields = ('name',)

    def get_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])

    get_categories.__name__ = 'Категории'


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryCharacteristic, CategoryCharacteristicAdmin)
