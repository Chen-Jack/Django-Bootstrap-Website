from django.conf.urls import url, include
from django.contrib import admin
from . import views as home_views
from account import urls as account_urls
from entry import urls as entry_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.HomeView.as_view() , name='main_page' ), #Home Page  
    url(r'^account/', include(account_urls)), #All account related urls
    url(r'^about/$', home_views.AboutView.as_view(), name='about'),
    url(r'^contact/$', home_views.ContactView.as_view(), name='contact'),
    url(r'^post/', include(entry_urls) ) ,
]
