# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from account.models import Entry
from .views import *
from .forms import *

# Create your views here.

class NewEntryView(CreateView):
    template_name = "new_entry.html"
    form_class = NewEntryForm
    context_object_name = 'form'
    def get_success_url(self):
        return reverse_lazy( "account:user", kwargs={"pk":self.request.user.id, "page":"1"})


class EntryDetailView(DetailView):
    template_name = 'entry_detail.html'
    context_object_name = 'entry'
    model = Entry

class DeleteEntryView(CreateView):
    pass