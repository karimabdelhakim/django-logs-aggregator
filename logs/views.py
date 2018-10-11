from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Log


@method_decorator(login_required, name='dispatch')
class ListLogsView(ListView):
    template_name = 'logs/list.html'
    paginate_by = 10

    def get_queryset(self):
        server_name = self.request.GET.get('q', None)
        if server_name:
            return Log.objects.get_server_logs(user=self.request.user, server_name=server_name)
        return Log.objects.get_user_logs(user=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['server_name'] = self.request.GET.get('q', None)
        # presist query paramas when paginating
        get_copy = self.request.GET.copy()
        query_params = get_copy.pop('page', True) and get_copy.urlencode()
        context_data['query_params'] = query_params

        return context_data
