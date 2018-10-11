from django.conf.urls import url

from .views import ListLogsView, ListServerLogsView

urlpatterns = [
    url(r'^$', ListLogsView.as_view(), name='list'),
    url(r'^(?P<server_name>[\w-]+)/$',
        ListServerLogsView.as_view(), name='list-server'),
]
