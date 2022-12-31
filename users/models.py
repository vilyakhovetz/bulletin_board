from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from users.managers import UserManager
from django.utils.html import format_html


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='users_photos/%Y/%m/%d', verbose_name='Фото пользователя', blank=True, null=True)
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_active = models.BooleanField(default=True, verbose_name='Активные пользователи')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def show_photo(self):
        return format_html(f'<img src="{self.photo.url}" width="150" height="150">') if self.photo else None

    show_photo.__name__ = "Предпросмотр"

    def show_phone(self):
        return f'+7 ({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:8]}-{self.phone_number[8:]}'

    show_phone.__name__ = "Предпросмотр"

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
