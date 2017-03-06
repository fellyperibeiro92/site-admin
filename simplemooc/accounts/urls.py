from django.conf.urls import url

from simplemooc.accounts import views as simplemoocviews
from django.contrib.auth import views

urlpatterns = [
  url(r'^/login/$', views.login,
    {
      'template_name': 'accounts/login.html'
    }
    , name='login'
  ),
  url(r'^/signup/$', simplemoocviews.signup
    , name='signup'
  )
]
