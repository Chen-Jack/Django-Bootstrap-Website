from django.conf.urls import url, include
from .views import *

app_name = "entry"

urlpatterns = [
    url(r'^new-post/$', NewEntryView.as_view() , name = 'new_post'),
    url(r'^detail/(?P<pk>[0-9]*)/$', EntryDetailView.as_view(), name='detail' ),
    url(r'^detail/(?P<pk>[0-9]*)/edit/$', EntryEditView.as_view() , name = 'edit'),
    url(r'^detail/(?P<pk>[0-9]*)/delete/$', EntryDeleteView.as_view(), name = 'delete'),
]