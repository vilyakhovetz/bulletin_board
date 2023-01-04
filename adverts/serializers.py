from rest_framework import serializers
from adverts.models import Advert, Category


class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user_detail_api', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Advert
        fields = ['id', 'author', 'title', 'category', 'content', 'price',
                  'publication_datetime', 'city', 'street', 'building_number']
