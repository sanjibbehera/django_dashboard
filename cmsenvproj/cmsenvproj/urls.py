"""cmsenvproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from cmsenvmgmt import views

router = routers.DefaultRouter()
#router.register(r'env_app', views.EnvappViewSet)
#router.register(r'e2e2appconfig', views.E2E2AppConfigViewSet)
#router.register(r'e2e1appconfig', views.E2E1AppConfigViewSet)
#router.register(r'e2e2dbconfig', views.E2E2DBConfigViewSet)
#router.register(r'e2e1dbconfig', views.E2E1DBConfigViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^cmsenvmgmt/', include('cmsenvmgmt.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
