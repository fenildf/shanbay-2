# -*- encoding: utf-8 -*-
from django.views.generic import View, TemplateView


class Index(TemplateView):
    template_name = 'index.html'
