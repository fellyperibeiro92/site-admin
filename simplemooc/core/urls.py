from django.conf.urls import url

from simplemooc.core import views

urlpatterns = [
  url(r'^$', views.home, name='home'), #r indicates to regularExp to Python
  url(r'^contact/$', views.contact, name='contact'),
]
