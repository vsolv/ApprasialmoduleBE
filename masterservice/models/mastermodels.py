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

class Country(models.Model):
    code = models.CharField(max_length=8, null=True, blank=True)
    name = models.CharField(max_length=64)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class State(models.Model):
    code = models.CharField(max_length=8, null=True, blank=True)
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class District(models.Model):
    code = models.CharField(max_length=8, null=True, blank=True)
    name = models.CharField(max_length=64)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class City(models.Model):
    code = models.CharField(max_length=8,null=True, blank=True)
    name = models.CharField(max_length=64)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Pincode(models.Model):
    district =models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    city =models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    no = models.CharField(max_length=8)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Goal(models.Model):
    goal = models.CharField(max_length=125)
    description = models.CharField(max_length=128, null=True, blank=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)