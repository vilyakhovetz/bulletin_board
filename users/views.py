from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, update_session_auth_hash, logout
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from users.models import User
from rest_framework import generics
from users.serializers import UserSerializer


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.photo = 'pfp.jpg'
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'


class UserDetailView(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'


@login_required(login_url='/users/login/')
def user_update_view(request, user_id):
    if user_id != request.user.id:
        raise PermissionDenied()
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.phone_number = form.cleaned_data['phone_number']
            if form.cleaned_data['photo']:
                request.user.photo = form.cleaned_data['photo']
            request.user.save()
            return redirect('profile', pk=request.user.id)
    else:
        default_data = {'first_name': request.user.first_name, 'last_name': request.user.last_name,
                        'email': request.user.email, 'phone_number': request.user.phone_number,
                        'photo': request.user.photo}
        form = UserUpdateForm(default_data)
    return render(request, 'users/update_profile.html', {'form': form})


@login_required(login_url='/users/login/')
def user_change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
