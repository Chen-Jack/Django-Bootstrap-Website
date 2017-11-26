from django.conf.urls import url, include
from .views import *

app_name = "entry"

urlpatterns = [
    url(r'^new-post/$', NewEntryView.as_view() , name = 'new_post'),
    url(r'^detail/(?P<pk>[0-9]*)/$', EntryDetailView.as_view(), name='detail' ),
]