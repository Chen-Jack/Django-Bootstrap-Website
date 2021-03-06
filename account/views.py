# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, FormView, View, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, mixins
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .forms import *

from .models import *

class AccountHomeView(mixins.LoginRequiredMixin, ListView):
    model = User

    def get_context_data(self,*args, **kwargs):

        page_value = int(self.kwargs['page'])
        next_page = page_value +1
        prev_page = page_value - 1
        request_user = self.request.user
        specified_user = User.objects.get(username = self.kwargs['username'])
        #Returns the only 10 entries per page
        qs = Entry.objects.filter(user=specified_user).order_by('time_created').reverse()[10*page_value-10 : 10*page_value]

        context = {'user': specified_user, 'request_user':request_user, 'entries':qs, 'next_page':next_page , 'prev_page':prev_page}
        return context

    def get_template_names(self):
        if(self.request.user.username == self.kwargs['username']):
            return 'account_home.html'
        else:
            return 'foreign_home.html'


class AccountRegisterView(CreateView):
    form_class = AccountForm
    template_name = 'registration_page.html'
    context_object_name = "form"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object = form.save()

        login( self.request, self.object)

        return HttpResponseRedirect(reverse_lazy( "account:user", kwargs={"username":self.object.username, "page":"1"}))
    
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self,*args, **kwargs):
        if( self.request.user.is_authenticated() ):
            return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"username":self.request.user.username, "page":"1"}))
        else:
            return render(self.request, self.template_name, {})
    
    
    def post(self, *args, **kwargs):
        filled_form = self.form_class(self.request.POST)

        if(filled_form.is_valid()):
            logged_in_user = authenticate(
                username = filled_form.cleaned_data['username'],
                password = filled_form.cleaned_data['password']
                )
            if(logged_in_user is not None):
                login(self.request, logged_in_user)
                return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"username":self.request.user.username, "page":"1"}))
            else:
                return HttpResponse("Incorrect Username/Password")
            
        else:
            return HttpResponse("Bad form input")

class LogOutView(View):
    
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect(reverse_lazy('main_page')) 

class SearchAccountView(ListView):
    context_object_name = "search"
    template_name = "search_results.html"

    def post(self, request, *args, **kwargs):
        print('form')

    def get_queryset(self, *args, **kwargs):
        query = self.kwargs['username']
        results = User.objects.filter(username__icontains = self.kwargs['username'])


        return {'query':query , 'results':results}

class AccountSettingsView(mixins.LoginRequiredMixin, TemplateView):    
    template_name = "account_settings.html"

class ChangePasswordView(mixins.LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'change_password.html'

    def form_valid(self,form):
        curr_user = self.request.user
        #Checking for correct password
        if not authenticate( username = curr_user, password = form.cleaned_data['old_password']):
            form.add_error(None, ValidationError( ('Incorrect Password'), code='invalid') )
            return super(ChangePasswordView, self).form_invalid(form)

        #Check if new password is identica
        if form.cleaned_data['new_password'] != form.cleaned_data['repeat_password']:
            form.add_error(None, ValidationError( ('Passwords did not match'), code='invalid') )
            return super(ChangePasswordView, self).form_invalid(form)

        curr_user.set_password(form.cleaned_data['new_password'])
        curr_user.save() #Is this needed?

        return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"username":self.request.user.username, "page":"1"}))

