# Generated by Django 2.2.4 on 2020-04-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client_rate_appointment',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='report_issue',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='request_client_contacts',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='request_reason',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
