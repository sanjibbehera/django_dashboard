from django.db import models

# Create your models here.
class Env_app(models.Model):
    environment_name = models.CharField(max_length=50)
    application_name = models.CharField(max_length=50)
    class Meta:
        ordering = ('environment_name',)
        
class Application_config(models.Model):
    environment_name            = models.CharField(max_length=50)
    application_name            = models.CharField(max_length=50)
    source_application          = models.CharField(max_length=100, null=True, blank=True)
    target_application          = models.CharField(max_length=100, null=True, blank=True)
    service_name                = models.CharField(max_length=200)
    operation_name              = models.CharField(max_length=200)
    service_name_version        = models.CharField(max_length=250)
    configuration_url           = models.CharField(max_length=1000)
    credentials_base64          = models.CharField(max_length=250)
    service_operation_health    = models.IntegerField()
    config_lastchange_date      = models.DateTimeField(auto_now_add=True)
