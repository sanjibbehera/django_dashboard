from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
#from websublime.contrib.manager.plus.sites import SitePlus
#admin.site = SitePlus()
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
]