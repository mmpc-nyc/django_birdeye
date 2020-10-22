# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.CharField(blank=True, null=True, max_length=128, validators=[validate_email], unique=True)
    phone = models.CharField(blank=True,null=True,max_length=11, unique=True)

    def __str__(self):
        return f'{self.email if self.email else self.phone}'

    def __unicode__(self):
        return f'{self.email if self.email else self.phone}'


class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(blank=False, null=False, max_length=32)
    last_name = models.CharField(blank=False, null=False, max_length=32)
    email = models.CharField(blank=True, null=True, max_length=128, validators=[validate_email], unique=True)
    phone = models.CharField(blank=True,null=True,max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'

    def __unicode__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'


class Checkin(models.Model):
    contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
