# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, View
from account.models import Entry
from django.contrib.auth import mixins
from .views import *
from .forms import *

# Create your views here.

class NewEntryView(mixins.LoginRequiredMixin, CreateView):
    template_name = "new_entry.html"
    form_class = EntryForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy( "account:user", kwargs={"pk":self.request.user.id, "page":"1"})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object = form.save()

        return HttpResponseRedirect(reverse_lazy( "account:user", kwargs={"pk":str(self.request.user.id), "page":"1"}))


class EntryDetailView(mixins.LoginRequiredMixin, DetailView):
    template_name = 'entry_detail.html'
    context_object_name = 'entry'
    model = Entry

class EntryEditView(mixins.LoginRequiredMixin, UpdateView):
    template_name = 'new_entry.html'
    form_class = EntryForm
    model = Entry

    def get_success_url(self):
        return reverse_lazy( "entry:detail", kwargs={"pk":self.object.id})
    

class EntryDeleteView(mixins.LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        obj = Entry.objects.filter(id = kwargs['pk'])
        obj.delete()
        return HttpResponseRedirect(reverse_lazy( "account:user", kwargs={"pk":self.request.user.id, "page":"1"}))