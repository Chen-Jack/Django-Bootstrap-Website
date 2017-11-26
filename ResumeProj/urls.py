from django.conf.urls import url, include
from django.contrib import admin
from . import views as home_views
from account import urls as account_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.HomeView.as_view() ), #Home Page  
    url(r'^account/', include(account_urls)), #All account related urls
]
