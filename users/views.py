from users.forms import UsersRegisterForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


def users_register_view(request):
    if request.method == 'POST':
        form = UsersRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UsersRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class UsersLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
