from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.decorators import login_required

from user.forms import LoginForm, RegisterForm
from user.models import Profile


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
            )
            Profile.objects.create(
                user=user,
                logo=form.cleaned_data['logo'],
                age=form.cleaned_data['age'],
                bio=form.cleaned_data['bio'],
            )

            return redirect('main_view')

        return render(request, 'user/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('main_view')
            form.add_error(None, 'Invalid username or password')

        return render(request, 'user/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_view')


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login_view')
        return render(request, 'user/profile.html')