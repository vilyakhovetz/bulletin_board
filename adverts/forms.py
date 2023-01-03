from django import forms
from django.forms import ModelForm
from adverts.models import Advert


cities = (('Москва', 'Москва'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Владивосток', 'Владивосток'))


class AdvertCreateForm(ModelForm):
    title = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '50',
                                      'placeholder': 'Введите название'}),
        required=True
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Введите краткое содержание объявления'}),
        required=True
    )
    price = forms.IntegerField(
        label='Цена',
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Введите цену'}),
        required=True
    )
    city = forms.CharField(
        label='Город',
        widget=forms.Select(attrs={'class': 'form-control',
                                   'placeholder': 'Выберите город',
                                   'required': True},
                            choices=cities)
    )
    street = forms.CharField(
        label='Улица',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '50',
                                      'placeholder': 'Введите название улицы'}),
        required=False
    )
    building_number = forms.IntegerField(
        label='Номер дома',
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'placeholder': 'Введите номер дома'}),
        required=False
    )

    class Meta:
        model = Advert
        fields = ('title', 'content', 'price', 'city', 'street', 'building_number')
