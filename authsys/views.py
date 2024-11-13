from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import  User
from .forms import SignInForm, SignUpForm

class SignUpView(CreateView):
    model = User
    template_name = 'authsys/register_page.html'
    form_class = SignUpForm
    success_url = reverse_lazy('get_to_main')
    extra_context = {'title': 'Регистрация'}


    def form_valid(self, form):
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'authsys/login_page.html'
    extra_context = {'title': 'Авторизация'}



    def get_success_url(self):
        return reverse_lazy('get_to_main')


def log(request):
    logout(request)
    return redirect('get_to_main')
