from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '100',
                                      'placeholder': 'Введите ваше имя'}),
        required=True
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '100',
                                      'placeholder': 'Введите вашу фамилию'}),
        required=True
    )
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '10',
                                      'minlength': '10',
                                      'placeholder': 'Введите номер телефона'}),
        required=True
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Введите адрес эл. почты'}),
        required=True
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Введите пароль'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Введите пароль еще раз'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Введите адрес эл. почты',
                                       'autofocus': True})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'autocomplete': 'current-password',
                                          'placeholder': 'Введите пароль'}),
    )


class UserUpdateForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '100',
                                      'placeholder': 'Введите ваше имя'}),
        required=True
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '100',
                                      'placeholder': 'Введите вашу фамилию'}),
        required=True
    )
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '10',
                                      'minlength': '10',
                                      'placeholder': 'Введите номер телефона'}),
        required=True
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Введите адрес эл. почты'}),
        required=True
    )
    photo = forms.ImageField(
        label='Изменить фото',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'photo')
