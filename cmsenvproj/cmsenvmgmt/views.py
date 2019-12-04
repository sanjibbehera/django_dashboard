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
    distinctenvapp = Env_app.objects.values('environment_name').distinct()
    return render(request, 'cmsenvmgmt/index.html', {'distinctenvapp' : distinctenvapp})