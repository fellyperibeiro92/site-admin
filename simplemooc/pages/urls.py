from django.conf.urls import url

from simplemooc.pages import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^/(?P<slug>[\w_-]+)/$', views.details, name='details')
  # r'^/(?P<_id>\d+)/$'
]
