# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin import register

from .models import Checkin
from .models import Contact
from .models import Employee


@register(Checkin)
class CheckinAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'contact_id', 'employee_id']


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id']


@register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']