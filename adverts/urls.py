from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from adverts.views import *

urlpatterns = [
    path('', adverts_list_view, name='index'),
    path('create_advert/', advert_create_view, name='create_advert'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
    path('my_adverts/', MyAdvertsView.as_view(), name='my_adverts'),
    path('advert/<int:advert_pk>/update/', advert_update_view, name='update_advert'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
