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
