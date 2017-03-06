"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# to load static files media
from django.conf import settings
from django.conf.urls.static import static


import simplemooc.core.urls
import simplemooc.courses.urls
import simplemooc.accounts.urls
import simplemooc.pages.urls

urlpatterns = [
  url(r'^', include(simplemooc.core.urls, namespace='core')), #r indicates to regularExp to Python
  url(r'^courses', include(simplemooc.courses.urls, namespace='courses')),
  url(r'^accounts', include(simplemooc.accounts.urls, namespace='accounts')),
  url(r'^pages', include(simplemooc.pages.urls, namespace='pages')),
  url(r'^admin/', admin.site.urls),
]

# if dev env
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
