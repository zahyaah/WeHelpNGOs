from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from datetime import datetime
import time


class HomePage(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'checkDateTime': datetime.now().strftime('%B %d, %Y'), 'checkTime': datetime.now().strftime("%H:%M:%S")}
