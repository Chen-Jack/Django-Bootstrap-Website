from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if(self.request.user.is_authenticated()):
            return HttpResponseRedirect(reverse_lazy('account:user', kwargs={"pk":str(self.request.user.id), 'page':'1'}))
        else:
            return super(HomeView, self).get(request, *args, **kwargs)

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'