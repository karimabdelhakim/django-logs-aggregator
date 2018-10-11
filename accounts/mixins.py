from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoggedUserRedirectMixin():
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('logs:list'))
        return super().get(*args, **kwargs)
