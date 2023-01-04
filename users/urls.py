from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_profile'),
    path('<int:user_id>/update', user_update_view, name='user_update'),
    path('change_password', user_change_password_view, name='user_change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_complete.html'), name='password_reset_complete'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
