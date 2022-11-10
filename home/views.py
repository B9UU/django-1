from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

class Login(LoginRequiredMixin, TemplateView):
    template_name = 'home/login.html'
    login_url = '/admin'

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()})

@login_required(login_url='/admin')
def login(request):
    return render(request, 'home/login.html', {})
