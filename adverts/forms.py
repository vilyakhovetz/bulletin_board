from django.forms import ModelForm
from adverts.models import Advert


class AdvertCreateForm(ModelForm):
    class Meta:
        model = Advert
        fields = ('title', 'content', 'price', 'city', 'street', 'building_number')
