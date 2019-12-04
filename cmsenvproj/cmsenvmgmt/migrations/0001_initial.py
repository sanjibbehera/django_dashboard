# Generated by Django 2.2.5 on 2019-12-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='E2E1_Application_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('sub_application', models.CharField(blank=True, max_length=50, null=True)),
                ('source_application', models.CharField(max_length=100)),
                ('target_application', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('operation_name', models.CharField(max_length=150)),
                ('service_name_version', models.CharField(max_length=150, null=True)),
                ('service_type', models.CharField(default='Webservice', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('application_support_type', models.CharField(default='Telefonica Environment Team Managed', max_length=50)),
                ('configuration_url', models.CharField(max_length=1000)),
                ('credentials_base64', models.CharField(max_length=150, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='E2E1_Application_config_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('sub_application', models.CharField(blank=True, max_length=50, null=True)),
                ('source_application', models.CharField(max_length=100)),
                ('target_application', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('operation_name', models.CharField(max_length=150)),
                ('service_name_version', models.CharField(max_length=150, null=True)),
                ('service_type', models.CharField(default='Webservice', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('application_support_type', models.CharField(default='Telefonica Environment Team Managed', max_length=50)),
                ('configuration_url', models.CharField(max_length=1000)),
                ('credentials_base64', models.CharField(max_length=150, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='E2E1_DB_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('stack_name', models.CharField(default='Enter Valid STACK Name', max_length=50)),
                ('database_name', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(default='DB', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('database_service_details', models.CharField(max_length=50, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
                ('database_package_name', models.CharField(default='Enter Valid DB Package Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='E2E1_DB_config_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('stack_name', models.CharField(default='Enter Valid STACK Name', max_length=50)),
                ('database_name', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(default='DB', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('database_service_details', models.CharField(max_length=50, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
                ('database_package_name', models.CharField(default='Enter Valid DB Package Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='E2E2_Application_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('sub_application', models.CharField(blank=True, max_length=50, null=True)),
                ('source_application', models.CharField(max_length=100)),
                ('target_application', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('operation_name', models.CharField(max_length=150)),
                ('service_name_version', models.CharField(max_length=150, null=True)),
                ('service_type', models.CharField(default='Webservice', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('application_support_type', models.CharField(default='Telefonica Environment Team Managed', max_length=50)),
                ('configuration_url', models.CharField(max_length=1000)),
                ('credentials_base64', models.CharField(max_length=150, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='E2E2_Application_config_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('sub_application', models.CharField(blank=True, max_length=50, null=True)),
                ('source_application', models.CharField(max_length=100)),
                ('target_application', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('operation_name', models.CharField(max_length=150)),
                ('service_name_version', models.CharField(max_length=150, null=True)),
                ('service_type', models.CharField(default='Webservice', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('application_support_type', models.CharField(default='Telefonica Environment Team Managed', max_length=50)),
                ('configuration_url', models.CharField(max_length=1000)),
                ('credentials_base64', models.CharField(max_length=150, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='E2E2_DB_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('stack_name', models.CharField(default='Enter Valid STACK Name', max_length=50)),
                ('database_name', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(default='DB', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('database_service_details', models.CharField(max_length=50, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
                ('database_package_name', models.CharField(default='Enter Valid DB Package Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='E2E2_DB_config_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
                ('stack_name', models.CharField(default='Enter Valid STACK Name', max_length=50)),
                ('database_name', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(default='DB', max_length=20)),
                ('service_health_information', models.CharField(default='Normal Services', max_length=4000)),
                ('database_service_details', models.CharField(max_length=50, null=True)),
                ('service_operation_health', models.IntegerField()),
                ('service_operation_healthcheckTimestamp', models.DateTimeField()),
                ('installation_downtime', models.IntegerField(default=0)),
                ('installation_startTimestamp', models.DateTimeField(null=True)),
                ('installation_finishTimestamp', models.DateTimeField(null=True)),
                ('service_operation_conf_lastchanged', models.DateTimeField(auto_now_add=True)),
                ('database_package_name', models.CharField(default='Enter Valid DB Package Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Env_app',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=20)),
                ('application_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('environment_name',),
                'unique_together': {('environment_name', 'application_name')},
            },
        ),
        migrations.AddConstraint(
            model_name='e2e2_db_config_history',
            constraint=models.CheckConstraint(check=models.Q(('stack_name', 'RCS STACK'), ('stack_name', 'OTHER STACK'), ('stack_name', 'TOOLS STACK'), _connector='OR'), name='check_constraint_stack_name'),
        ),
        migrations.AlterUniqueTogether(
            name='e2e2_db_config_history',
            unique_together={('environment_name', 'application_name', 'database_name', 'service_name', 'service_type')},
        ),
        migrations.AddConstraint(
            model_name='e2e2_db_config',
            constraint=models.CheckConstraint(check=models.Q(('stack_name', 'RCS STACK'), ('stack_name', 'OTHER STACK'), ('stack_name', 'TOOLS STACK'), _connector='OR'), name='check_constraint_stack_name'),
        ),
        migrations.AlterUniqueTogether(
            name='e2e2_db_config',
            unique_together={('environment_name', 'application_name', 'database_name', 'service_name', 'service_type')},
        ),
        migrations.AlterUniqueTogether(
            name='e2e2_application_config_history',
            unique_together={('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url')},
        ),
        migrations.AlterUniqueTogether(
            name='e2e2_application_config',
            unique_together={('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url')},
        ),
        migrations.AddConstraint(
            model_name='e2e1_db_config_history',
            constraint=models.CheckConstraint(check=models.Q(('stack_name', 'RCS STACK'), ('stack_name', 'OTHER STACK'), ('stack_name', 'TOOLS STACK'), _connector='OR'), name='check_constraint_stack_name'),
        ),
        migrations.AlterUniqueTogether(
            name='e2e1_db_config_history',
            unique_together={('environment_name', 'application_name', 'database_name', 'service_name', 'service_type')},
        ),
        migrations.AddConstraint(
            model_name='e2e1_db_config',
            constraint=models.CheckConstraint(check=models.Q(('stack_name', 'RCS STACK'), ('stack_name', 'OTHER STACK'), ('stack_name', 'TOOLS STACK'), _connector='OR'), name='check_constraint_stack_name'),
        ),
        migrations.AlterUniqueTogether(
            name='e2e1_db_config',
            unique_together={('environment_name', 'application_name', 'database_name', 'service_name', 'service_type')},
        ),
        migrations.AlterUniqueTogether(
            name='e2e1_application_config_history',
            unique_together={('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url')},
        ),
        migrations.AlterUniqueTogether(
            name='e2e1_application_config',
            unique_together={('environment_name', 'application_name', 'sub_application', 'service_name', 'operation_name', 'service_name_version', 'configuration_url')},
        ),
    ]
