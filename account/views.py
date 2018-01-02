# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, FormView, View, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, mixins
from django.forms import ModelForm
from .forms import *

from .models import *

class AccountHomeView(mixins.LoginRequiredMixin, ListView):
    model = User
    template_name = 'account_home.html'
    def get_context_data(self,*args, **kwargs):
        page_value = int(self.kwargs['page'])
        next_page = page_value +1
        prev_page = page_value - 1
        specified_user = User.objects.get(id = self.kwargs['pk'])
        #Returns the only 10 entries per page
        qs = Entry.objects.filter(user=specified_user).order_by('time_created').reverse()[10*page_value-10 : 10*page_value]

        context = {'user': specified_user, 'entries':qs, 'next_page':next_page , 'prev_page':prev_page}
        return context
    
class AccountRegisterView(CreateView):
    form_class = AccountForm
    template_name = 'registration_page.html'
    context_object_name = "form"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password']);
        self.object = form.save()

        login( self.request, self.object)

        return HttpResponseRedirect(reverse_lazy( "account:user", kwargs={"pk":str(self.object.id), "page":"1"}))
    
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self,*args, **kwargs):
        if( self.request.user.is_authenticated() ):
            return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"pk":str(self.request.user.id), "page":"1"}))
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
                return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"pk":str(logged_in_user.id), "page":"1"}))
            else:
                return HttpResponse("Incorrect Username/Password")
            
        else:
            return HttpResponse("Bad form input")

class LogOutView(View):
    
    def get(self, request):
        logout(self.request)
        print('logging off')
        return HttpResponseRedirect(reverse_lazy('main_page'))