from django.conf.urls import url, include
from .views import *

app_name = "account"

urlpatterns = [
    url(r'^home/$', LoginView.as_view()),
    url(r'^home/(?P<pk>[0-9]*)/$', AccountHomeView.as_view(), name="home"),
    url(r'^login/$', LoginView.as_view(), name = "login"),
    url(r'^logout/$', LogOutView.as_view() ,name='logout'),
    url(r'^register/$', AccountRegisterView.as_view(), name="register"),
]