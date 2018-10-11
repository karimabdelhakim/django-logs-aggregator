from django.conf.urls import url

from .views import CreateLogView

urlpatterns = [
    url(r'^create/$', CreateLogView.as_view(), name='create'),
]
