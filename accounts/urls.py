from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from .views import CreateUserView, LoginUserView

urlpatterns = [
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^login/$', LoginUserView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),
]
