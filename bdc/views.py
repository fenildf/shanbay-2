from django.views.generic import View
from django.http import HttpResponse


class Index(View):
    def get(self, request):
        return HttpResponse("Hello world!")
