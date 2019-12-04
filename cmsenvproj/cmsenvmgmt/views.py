from django.shortcuts import render
from .models import Env_app, E2E2_Application_config, E2E1_Application_config, E2E2_DB_config, E2E1_DB_config

# Create your views here.

def index(request):
    distinctenvapp = Env_app.objects.values('environment_name').distinct()
    return render(request, 'envconfmgmt/index.html', {'distinctenvapp' : distinctenvapp});