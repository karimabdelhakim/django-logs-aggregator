from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Log


@method_decorator(login_required, name='dispatch')
class ListLogsView(ListView):
    template_name = 'logs/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Log.objects.get_user_logs(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ListServerLogsView(ListView):
    template_name = 'logs/list.html'
    paginate_by = 10

    def get_queryset(self):
        server_name = self.kwargs.get('server_name')
        return Log.objects.get_server_logs(user=self.request.user, server_name=server_name)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['server_name'] = self.kwargs.get('server_name')
        return context_data
