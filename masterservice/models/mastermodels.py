from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now



class Department(models.Model):
    code = models.CharField(max_length=8, unique=True, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    # branch = models.ForeignKey(EmployeeBranch, on_delete=models.SET_NULL, null=True)
    # dept_id = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    # short_notation = models.CharField(max_length=8, null=True, blank=True)
    # is_sys = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)