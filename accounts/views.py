from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import CreateUserForm, LoginUserForm
from .mixins import LoggedUserRedirectMixin


class CreateUserView(LoggedUserRedirectMixin, CreateView):
    template_name = 'accounts/login-register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


class LoginUserView(LoggedUserRedirectMixin, FormView):
    form_class = LoginUserForm
    success_url = reverse_lazy('logs:list')
    template_name = 'accounts/login-register.html'

    def form_valid(self, form):
        if form.is_valid():
            login(self.request, form.user)
            return super().form_valid(form)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
