from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from adverts.views import AdvertListView, adverts_create_view

urlpatterns = [
    path('', AdvertListView.as_view(), name='index'),
    path('create_advert/', adverts_create_view, name='create_advert'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
