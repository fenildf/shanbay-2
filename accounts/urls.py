from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AccountView.as_view(), name='index')
]
