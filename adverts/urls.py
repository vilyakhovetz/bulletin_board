from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from adverts.views import AdvertListView, adverts_create_view, AdvertDetailView

urlpatterns = [
    path('', AdvertListView.as_view(), name='index'),
    path('create_advert/', adverts_create_view, name='create_advert'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
