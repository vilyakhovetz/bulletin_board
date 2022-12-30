from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from adverts.views import AdvertListView

urlpatterns = [path('', AdvertListView.as_view(), name='index'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
