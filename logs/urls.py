from django.conf.urls import url

from .views import ListLogsView

urlpatterns = [
    url(r'^$', ListLogsView.as_view(), name='list'),
]
