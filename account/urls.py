from django.conf.urls import url, include
from .views import *
from entry import urls as entry_urls

app_name = "account"

urlpatterns = [
    url(r'^home/$', LoginView.as_view()),
    url(r'^home/user/(?P<username>\w*)/(?P<page>[0-9]*)$', AccountHomeView.as_view(), name="user"),
    url(r'^login/$', LoginView.as_view(), name = "login"),
    url(r'^logout/$', LogOutView.as_view() ,name='logout'),
    url(r'^register/$', AccountRegisterView.as_view(), name="register"),
    url(r'^search/(?P<username>\w*)/$', SearchAccountView.as_view(),  name = "search"),

]