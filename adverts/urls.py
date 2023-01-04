from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from adverts.views import *
from users import views as users_views

urlpatterns = [
    path('', adverts_list_view, name='index'),
    path('create_advert/', advert_create_view, name='create_advert'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
    path('my_adverts/', MyAdvertsView.as_view(), name='my_adverts'),
    path('advert/<int:advert_pk>/update/', advert_update_view, name='update_advert'),
    path('advert/<int:pk>/delete/', AdvertDeleteView.as_view(), name='delete_advert'),
    path('api/', api_root),
    path('api/adverts/', AdvertListAPI.as_view(), name='adverts_list_api'),
    path('api/advert/<int:pk>/', AdvertDetailAPI.as_view(), name='advert_detail_api'),
    path('api/users/', users_views.UserListAPI.as_view(), name='users_list_api'),
    path('api/user/<int:pk>/', users_views.UserDetailAPI.as_view(), name='user_detail_api'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
