from django.http import HttpResponse
from django.views.generic import View, TemplateView


class Index(TemplateView):
    template_name = 'bdc/index.html'
