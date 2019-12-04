from django.shortcuts import render
from .models import Env_app, E2E2_Application_config, E2E1_Application_config, E2E2_DB_config, E2E1_DB_config
from django.contrib import admin
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from django.db import connection
from django.db.models import Count, Q
import json as simplejson
from rest_framework import viewsets
from django.utils import timezone
import pytz
import datetime

# Create your views here.

def index(request):
    e2e1appnos = Env_app.objects.filter(environment_name='E2E1').count()
    e2e2appnos = Env_app.objects.filter(environment_name='E2E2').count()
    e2e1dbnos = Env_app.objects.filter(environment_name='E2E1 DB').count()
    e2e2dbnos = Env_app.objects.filter(environment_name='E2E2 DB').count()
    return render(request, 'cmsenvmgmt/index.html', {'e2e1appnos' : e2e1appnos, 'e2e2appnos' : e2e2appnos, 'e2e1dbnos' : e2e1dbnos, 'e2e2dbnos' : e2e2dbnos})