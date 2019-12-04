from django.db import models

# Create your models here.
class Env_app(models.Model):
    environment_name = models.CharField(max_length=20)
    application_name = models.CharField(max_length=50)
    class Meta:
        ordering = ('environment_name',)
        unique_together = (('environment_name', 'application_name'),)

class E2E2_DB_config(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    stack_name 				= models.CharField(max_length=50, default='Enter Valid STACK Name')
    database_name 				= models.CharField(max_length=50)
    service_name 				= models.CharField(max_length=100)
    service_type 				= models.CharField(max_length=20, default='DB')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    database_service_details    = models.CharField(max_length=50, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    database_package_name 		= models.CharField(max_length=50, default='Enter Valid DB Package Name')
    class Meta:
        unique_together = (('environment_name', 'application_name', 'database_name', 'service_name', 'service_type'),)
        constraints = [
            models.CheckConstraint(check=(models.Q(stack_name="RCS STACK") | models.Q(stack_name="OTHER STACK") | models.Q(stack_name="TOOLS STACK")), name='check_constraint_stack_name'),
        ]

class E2E2_DB_config_history(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    stack_name 				= models.CharField(max_length=50, default='Enter Valid STACK Name')
    database_name 				= models.CharField(max_length=50)
    service_name 				= models.CharField(max_length=100)
    service_type 				= models.CharField(max_length=20, default='DB')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    database_service_details    = models.CharField(max_length=50, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    database_package_name 		= models.CharField(max_length=50, default='Enter Valid DB Package Name')
    class Meta:
        unique_together = (('environment_name', 'application_name', 'database_name', 'service_name', 'service_type'),)
        constraints = [
            models.CheckConstraint(check=(models.Q(stack_name="RCS STACK") | models.Q(stack_name="OTHER STACK") | models.Q(stack_name="TOOLS STACK")), name='check_constraint_stack_name'),
        ]

class E2E1_DB_config(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    stack_name 				= models.CharField(max_length=50, default='Enter Valid STACK Name')
    database_name 				= models.CharField(max_length=50)
    service_name 				= models.CharField(max_length=100)
    service_type 				= models.CharField(max_length=20, default='DB')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    database_service_details    = models.CharField(max_length=50, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    database_package_name 		= models.CharField(max_length=50, default='Enter Valid DB Package Name')
    class Meta:
        unique_together = (('environment_name', 'application_name', 'database_name', 'service_name', 'service_type'),)
        constraints = [
            models.CheckConstraint(check=(models.Q(stack_name="RCS STACK") | models.Q(stack_name="OTHER STACK") | models.Q(stack_name="TOOLS STACK")), name='check_constraint_stack_name'),
        ]

class E2E1_DB_config_history(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    stack_name 				= models.CharField(max_length=50, default='Enter Valid STACK Name')
    database_name 				= models.CharField(max_length=50)
    service_name 				= models.CharField(max_length=100)
    service_type 				= models.CharField(max_length=20, default='DB')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    database_service_details    = models.CharField(max_length=50, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    database_package_name 		= models.CharField(max_length=50, default='Enter Valid DB Package Name')
    class Meta:
        unique_together = (('environment_name', 'application_name', 'database_name', 'service_name', 'service_type'),)
        constraints = [
            models.CheckConstraint(check=(models.Q(stack_name="RCS STACK") | models.Q(stack_name="OTHER STACK") | models.Q(stack_name="TOOLS STACK")), name='check_constraint_stack_name'),
        ]

class E2E2_Application_config(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    sub_application  				= models.CharField(max_length=50, null=True, blank=True)
    source_application 				= models.CharField(max_length=100)
    target_application 				= models.CharField(max_length=100)
    service_name 				= models.CharField(max_length=100)
    operation_name 				= models.CharField(max_length=150)
    service_name_version 			= models.CharField(max_length=150, null=True)
    service_type 				= models.CharField(max_length=20, default='Webservice')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    application_support_type 			= models.CharField(max_length=50, default='Telefonica Environment Team Managed')
    configuration_url 				= models.CharField(max_length=1000)
    credentials_base64 				= models.CharField(max_length=150, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url'),)

class E2E2_Application_config_history(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    sub_application  				= models.CharField(max_length=50, null=True, blank=True)
    source_application 				= models.CharField(max_length=100)
    target_application 				= models.CharField(max_length=100)
    service_name 				= models.CharField(max_length=100)
    operation_name 				= models.CharField(max_length=150)
    service_name_version 			= models.CharField(max_length=150, null=True)
    service_type 				= models.CharField(max_length=20, default='Webservice')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    application_support_type 			= models.CharField(max_length=50, default='Telefonica Environment Team Managed')
    configuration_url 				= models.CharField(max_length=1000)
    credentials_base64 				= models.CharField(max_length=150, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url'),)

class E2E1_Application_config(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    sub_application  				= models.CharField(max_length=50, null=True, blank=True)
    source_application 				= models.CharField(max_length=100)
    target_application 				= models.CharField(max_length=100)
    service_name 				= models.CharField(max_length=100)
    operation_name 				= models.CharField(max_length=150)
    service_name_version 			= models.CharField(max_length=150, null=True)
    service_type 				= models.CharField(max_length=20, default='Webservice')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    application_support_type 			= models.CharField(max_length=50, default='Telefonica Environment Team Managed')
    configuration_url 				= models.CharField(max_length=1000)
    credentials_base64 				= models.CharField(max_length=150, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url'),)

class E2E1_Application_config_history(models.Model):
    environment_name 				= models.CharField(max_length=20)
    application_name 				= models.CharField(max_length=50)
    sub_application  				= models.CharField(max_length=50, null=True, blank=True)
    source_application 				= models.CharField(max_length=100)
    target_application 				= models.CharField(max_length=100)
    service_name 				= models.CharField(max_length=100)
    operation_name 				= models.CharField(max_length=150)
    service_name_version 			= models.CharField(max_length=150, null=True)
    service_type 				= models.CharField(max_length=20, default='Webservice')
    service_health_information				= models.CharField(max_length=4000, default='Normal Services')
    application_support_type 			= models.CharField(max_length=50, default='Telefonica Environment Team Managed')
    configuration_url 				= models.CharField(max_length=1000)
    credentials_base64 				= models.CharField(max_length=150, null=True)
    service_operation_health 			= models.IntegerField()
    service_operation_healthcheckTimestamp 	= models.DateTimeField()
    installation_downtime 			= models.IntegerField(default=0)
    installation_startTimestamp 		= models.DateTimeField(null=True)
    installation_finishTimestamp 		= models.DateTimeField(null=True)
    service_operation_conf_lastchanged 		= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url'),)