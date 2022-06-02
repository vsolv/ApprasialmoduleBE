# Generated by Django 3.0.4 on 2022-05-25 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeservice', '0005_auto_20220524_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeaddress',
            name='type',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeepersionalinfo',
            name='emc_contact_person_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\?1?\\d{9,10}$')]),
        ),
    ]
