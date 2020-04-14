# Generated by Django 2.2.4 on 2020-04-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190821_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_number',
            field=models.CharField(max_length=16, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
