from django.urls import path
from users.views import users_register_view, UsersLoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', users_register_view, name='register'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
