# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, FormView, View, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from .forms import *

from .models import *

class AccountHomeView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'account_home.html'

class AccountRegisterView(CreateView):
    form_class = AccountForm
    template_name = 'registration_page.html'
    context_object_name = "form"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password']);
        self.object = form.save()

        return HttpResponseRedirect(reverse_lazy( "account:home", kwargs={"pk":str(self.object.id)}))
    
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self,*args, **kwargs):
        if( self.request.user.is_authenticated() ):
            return HttpResponseRedirect(reverse_lazy('account:home', kwargs={"pk":str(self.request.user.id)}))
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
                return HttpResponseRedirect(reverse_lazy('account:home', kwargs={"pk":str(logged_in_user.id)}))
            else:
                pass
            
        else:
            return HttpResponse("Bad form input")