from users.models import User
from rest_framework import serializers
from adverts.models import Advert


class UserSerializer(serializers.HyperlinkedModelSerializer):
    adverts = serializers.HyperlinkedRelatedField(many=True, view_name='advert_detail_api', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'date_joined', 'adverts']
