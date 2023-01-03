from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('<int:user_id>/update', user_update_view, name='update')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
