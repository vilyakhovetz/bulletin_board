from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
