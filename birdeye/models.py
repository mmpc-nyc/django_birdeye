# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Checkin(models.Model):
    timestamp = models.DateTimeField(null=True,blank=True)
    contactid = models.IntegerField(blank=False,null=False)
    employeeid = models.IntegerField(blank=False,null=False)
    employee_email = models.CharField(blank=True,null=True,max_length=128)
    customer_email = models.CharField(blank=True,null=True,max_length=128)
    phone = models.CharField(blank=True,null=True,max_length=11)
